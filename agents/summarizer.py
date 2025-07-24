# agents/summarizer.py


from crewai import Agent
from tools.scraper_tool import scraper_tool

def create_summarizer_agent(llm):
    """
    Creates the Summarizer Agent.
    This agent is responsible for scraping and summarizing web content.
    """
    return Agent(
        role='Content Summarization Specialist',
        goal='Scrape and distill the key information from web pages into concise, easy-to-understand summaries.',
        backstory=(
            "You are an expert analyst with a talent for cutting through the noise. "
            "You can quickly read through dense web content, identify the core arguments and facts, "
            "and present them in a clear and structured summary."
        ),
        tools=[scraper_tool],
        llm=llm,
        verbose=True,
        allow_delegation=False
    )