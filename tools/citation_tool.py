# tools/citation_tool.py

from crewai_tools import BaseTool
from datetime import datetime

class CitationTool(BaseTool):
    name: str = "Citation Generator"
    description: str = "Generates a citation for a given URL with the access timestamp."

    def _run(self, url: str) -> str:
        """
        Generates a simple citation for a URL.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"[{url}] (Accessed on {timestamp})"

# Instantiate the citation tool
citation_tool = CitationTool()