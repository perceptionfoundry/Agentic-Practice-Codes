from pydantic import BaseModel
from agents import Agent


HOW_MANY_SEARCHES = 3

INSTRUCTION = f"You are a helpful research assitant. Given a query, compose up with a set of web search \
    to perform to best answer the query. Output {HOW_MANY_SEARCHES} term to query for."

class WebSearchItem(BaseModel):
    reason: str
    "Your reasoning for why this search is important to the query"
    
    query: str
    "The search term to use for the web search"

class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem]
    """A list of web searches to perform to best answer the query"""

planner_agent = Agent(
    name="PlannerAgent",
    instructions=INSTRUCTION,
    model="gpt-4o-mini",
    output_type=WebSearchPlan
    
)