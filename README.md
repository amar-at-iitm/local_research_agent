# Local Autonomous Research Agent

An offline-capable research agent that autonomously performs multi-step web research to generate structured reports with citations. This agent is designed to run locally, ensuring data privacy and control over the research process.

## Problem Statement
The goal of this project is to build a research agent that can take a topic query and perform comprehensive, multi-step web research without relying on external cloud services for its core intelligence. The agent will use locally hosted LLMs to browse, search, collect, and analyze information, ultimately producing a well-structured and cited report.

## Features
- **Offline-First:** All language model processing is done locally using GPT-OSS-20B.
- **Multi-Agent System:** Utilizes a manager-worker architecture for efficient task delegation and execution.
- **Autonomous Web Research:** Can perform multi-step research using search and browsing tools.
- **Structured Reporting:** Generates reports in various formats (PDF, Markdown, HTML) with an executive summary, key findings, and citations.
- **Transparent Reasoning:** Keeps detailed logs of its reasoning process for auditability and transparency.
- **Configurable & Extensible:** The agent's toolset and pipeline can be easily modified and extended.

## Architecture
The agent operates on a multi-agent framework, inspired by methodologies like CrewAI and LangGraph. This architecture consists of a **Manager Agent** that orchestrates a team of specialized **Worker Agents**:

- **Manager Agent:** The "brains" of the operation. Receives the initial research query, breaks it into a research plan, and assigns tasks to worker agents.
- **Searcher Agent:** Executes web searches based on the research plan.
- **Summarizer Agent:** Scrapes and summarizes web pages to extract relevant information.
- **Writer Agent:** Compiles extracted information into a structured report, complete with an executive summary, key findings, and citations.

**Workflow:**
1. User provides a research topic.
2. Manager Agent creates a research plan.
3. Searcher Agent retrieves relevant URLs.
4. Summarizer Agent extracts key facts from each source.
5. Writer Agent generates the final report.

## Technology Stack
- **LLM:** GPT-OSS-20B
- **LLM Serving:** vLLM or Hugging Face Transformers
- **Agent Framework:** CrewAI / LangGraph (or a custom implementation)
- **Web Scraping:** BeautifulSoup / Scrapy
- **Search:** DuckDuckGo Search API (or other search API)

## Getting Started

### Prerequisites
- Python 3.8+
- A machine with sufficient resources to run GPT-OSS-20B (GPU with at least 24GB VRAM recommended).

### 1. Clone the Repository
```bash
git clone https://github.com/amar-at-iitm/local_research_agent
cd local-research-agent
````

### 2. Set Up the Local LLM

You can set up GPT-OSS-20B using **vLLM** or **Hugging Face Transformers**.

**Option A: Using vLLM (Recommended)**

```bash
pip install vllm
python -m vllm.entrypoints.openai.api_server --model "gpt-oss/gpt-oss-20b"
```

**Option B: Using Hugging Face Transformers**

```bash
pip install transformers torch
```

Configure the project to load the model via the Transformers pipeline.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```
OPENAI_API_BASE="http://localhost:8000/v1"
OPENAI_API_KEY="your-api-key"
DUCKDUCKGO_API_KEY="your-duckduckgo-api-key"
```

## Usage

Run a research task:

```bash
python main.py "Your research topic"
```

With optional constraints:

```bash
python main.py "Impact of AI on climate change" --format pdf --time-window "2022-2024"
```

## Project Structure

```
.
├── main.py                 # Main entry point
├── agents/
│   ├── manager.py
│   ├── searcher.py
│   ├── summarizer.py
│   └── writer.py
├── tools/
│   ├── search_tool.py
│   ├── scraper_tool.py
│   └── citation_tool.py
├── reports/                # Generated reports
├── logs/                   # Reasoning logs
├── examples/               # Example reports
├── requirements.txt
└── README.md
```

## Outputs

* Structured report in `reports/` (Markdown, PDF, or HTML)
* Executive Summary
* Key Findings
* References (URLs + timestamps)
* JSON metadata file in `logs/` containing the full reasoning chain

