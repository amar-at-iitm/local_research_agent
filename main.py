#  main.py

import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI
from agents.manager import ResearchCrew
from datetime import datetime

def setup_llm():
    """
    Sets up the local Language Model client.
    Assumes a vLLM or similar server running that mimics the OpenAI API.
    """
    # Load environment variables from .env file
    load_dotenv()
    
    api_base = os.getenv("OPENAI_API_BASE", "http://localhost:8000/v1")
    api_key = os.getenv("OPENAI_API_KEY", "not-needed") # API key is often not needed for local servers

    # Point the OpenAI client to the local server
    llm = OpenAI(base_url=api_base, api_key=api_key).chat.completions
    return llm

def main():
    """
    Main function to run the research agent.
    """
    # --- Argument Parsing ---
    parser = argparse.ArgumentParser(description="Local Autonomous Research Agent")
    parser.add_argument("topic", type=str, help="The research topic.")
    parser.add_argument("--format", type=str, default="md", choices=["md", "pdf", "html"], help="Output report format.")
    parser.add_argument("--time-window", type=str, help="Optional time window for research (e.g., '2022-2024').")
    args = parser.parse_args()

    print(f" Starting research on topic: '{args.topic}'")

    # --- Directory Setup ---
    # Ensure output directories exist
    os.makedirs("reports", exist_ok=True)
    os.makedirs("logs", exist_ok=True)

    # --- LLM and Crew Initialization ---
    try:
        llm = setup_llm()
        research_crew = ResearchCrew(llm)
    except Exception as e:
        print(f" Error setting up the LLM or Crew: {e}")
        return

    # --- Run the Crew ---
    try:
        report, usage_metrics = research_crew.run(args.topic, args.time_window)
        
        print("\n\n Research complete!")
        print(" LLM Usage Metrics:")
        print(usage_metrics)

        # --- Save Outputs ---
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        topic_slug = args.topic.replace(" ", "_").lower()[:30]
        
        # Save the final report
        report_filename = f"reports/{topic_slug}_{timestamp}.{args.format}"
        with open(report_filename, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"\n Report saved to: {report_filename}")

        # Save the logs/metadata (usage_metrics in this case)
        log_filename = f"logs/{topic_slug}_{timestamp}_log.json"
        with open(log_filename, "w", encoding="utf-8") as f:
            import json
            json.dump(usage_metrics, f, indent=4)
        print(f" Logs saved to: {log_filename}")

    except Exception as e:
        print(f" An error occurred during the research process: {e}")

if __name__ == "__main__":
    main()

