# agents/writer.py


from crewai import Agent
from tools.citation_tool import citation_tool

def create_writer_agent(llm):
    """
    Creates the Writer Agent.
    This agent is responsible for compiling the final research report.
    """
    return Agent(
        role='Professional Report Writer',
        goal='Compose a comprehensive, well-structured, and properly cited research report from the collected data.',
        backstory=(
            "You are a skilled writer and editor, known for your ability to transform raw data and summaries "
            "into polished, professional reports. Your work is characterized by clarity, accuracy, and meticulous "
            "attention to detail, including proper citations for all sources."
        ),
        tools=[citation_tool],
        llm=llm,
        verbose=True,
        allow_delegation=False
    )

