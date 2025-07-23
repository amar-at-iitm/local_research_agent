# tools/scraper_tool.py

from crewai_tools import ScrapeWebsiteTool

# Instantiate the scraper tool
# You can pass a specific website URL if you want the tool to be dedicated to one site
# For general purpose scraping, we don't need to pass a URL here.
scraper_tool = ScrapeWebsiteTool()