from pydantic import BaseModel
from agents import Agent

INSTRUCTION = (
    "You are a senior researcher tasked with writing a cohesive report for a research query."
    "You will be provided with the original query, and some initial research done by a research assistant.\n"
    "You should first come up with an outline for the report that describes the structure and"
    "The final output should ne in markdown format, and it should be lengthy and detailed. Aim"
    "for 5-10 pages of content, at least 1000 words"
)

class ReportData(BaseModel):
    short_summary: str
    """A short 2-3 sentence summary of the finding"""
    
    markdown_report : str
    """The final report"""
    
    follow_up_questions: list[str]
    """ Suggested topics to research further"""
    
writer_agent = Agent(
    name="WriterAgent",
    instructions=INSTRUCTION,
    model="gpt-4o-mini",
    output_type=ReportData
)
