#  agents/manager.py



from crewai import Crew, Process, Task
from agents.searcher import create_searcher_agent
from agents.summarizer import create_summarizer_agent
from agents.writer import create_writer_agent

class ResearchCrew:
    def __init__(self, llm):
        self.llm = llm
        self.searcher = create_searcher_agent(llm)
        self.summarizer = create_summarizer_agent(llm)
        self.writer = create_writer_agent(llm)

    def create_tasks(self, topic, time_window=None):
        """
        Creates the tasks for the research crew.
        """
        # Task for the Searcher Agent
        search_task = Task(
            description=(
                f"Search the web for credible and relevant information on the topic: '{topic}'. "
                f"If a time window is specified, focus on results from that period: {time_window if time_window else 'N/A'}. "
                "Compile a list of the top 5-7 most promising URLs."
            ),
            expected_output="A list of 5-7 relevant URLs.",
            agent=self.searcher,
        )

        # Task for the Summarizer Agent
        summarize_task = Task(
            description=(
                "For each URL provided by the searcher, scrape the content and create a concise summary. "
                "Focus on extracting key facts, figures, and main arguments. "
                "The summaries should be clear and easy to digest."
            ),
            expected_output="A compiled list of summaries, with each summary corresponding to a URL.",
            agent=self.summarizer,
            context=[search_task] # This task depends on the output of the search_task
        )

        # Task for the Writer Agent
        write_task = Task(
            description=(
                "Using the provided summaries and URLs, write a comprehensive research report on the topic: '{topic}'. "
                "The report should have an executive summary, a body with key findings (in bullet points), "
                "and a conclusion. Ensure every piece of information is attributed to its source by generating a citation "
                "for each URL used. The final output should be a well-formatted Markdown document."
            ),
            expected_output=f"A structured research report on '{topic}' in Markdown format, complete with an executive summary, key findings, and citations.",
            agent=self.writer,
            context=[summarize_task] # This task depends on the output of the summarize_task
        )

        return [search_task, summarize_task, write_task]

    def run(self, topic, time_window=None):
        """
        Initializes and runs the research crew.
        """
        tasks = self.create_tasks(topic, time_window)
        
        crew = Crew(
            agents=[self.searcher, self.summarizer, self.writer],
            tasks=tasks,
            process=Process.sequential,
            verbose=2 # Set to 2 for detailed execution logs
        )

        result = crew.kickoff()
        return result, crew.usage_metrics
