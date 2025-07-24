# agents/searcher.py
from crewai import Agent
from tools.search_tool import search_tool

def create_searcher_agent(llm):
    """
    Creates the Searcher Agent.
    This agent is responsible for finding relevant information on the web.
    """
    return Agent(
        role='Expert Web Searcher',
        goal='Find the most relevant and up-to-date information on a given research topic.',
        backstory=(
            "As a meticulous and efficient digital librarian, you excel at crafting precise search queries "
            "and identifying the most credible and relevant sources from the vast expanse of the internet. "
            "Your skills are crucial for laying the foundation of any research task."
        ),
        tools=[search_tool],
        llm=llm,
        verbose=True,
        allow_delegation=False
    )
