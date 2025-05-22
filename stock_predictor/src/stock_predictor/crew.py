from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from pydantic import BaseModel, Field
from typing import List
from crewai.tools import SerperDevtool


class TrendingCompany(BaseModel):
    """ A company that is in the news and attracting attention """
    name:str = Field(description="Company name")
    ticker: str = Field(description="Stocker ticker symbol")
    reason: str = Field(description="Reason this company is trending in the news")
    
class TrendingCompanyList(BaseModel):
    """ List of multiple trending companies that are in the news """
    companies: List[TrendingCompany] = Field(description="Listof companies trending in the news")
    
class TrendingCompanyResearch(BaseModel):
    """ Detailed research on a company """
    name: str = Field(description="Company Name")
    market_position: str = Field(description="Current market position and competitive analysis")
    future_outlook: str = Field(descrition="Future outlook and growth prospects")
    investment_potential: str = Field(description="Investment potential an suitability for investment")
    
class TrendingCompanyResearchList(BaseModel):
    """ A list of detailed research on all the companies """
    research_list: List[TrendingCompanyResearch] = Field(description= " Comprehesive research on all trending companies")
    
    

@CrewBase
class StockPredictor():
    """StockPredictor crew"""
    
    agent_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    @agent
    def trending_company_find(self) -> Agent:
        return Agent(config=self.agent_config['trending_company_finder'], tools=[SerperDevtool()])
    
    @agent
    def financial_researcher(self) -> Agent:
        return Agent(config=self.agent_config['financial_researcher'], tools=[SerperDevtool()])

    @agent
    def stock_picker(self) -> Agent:
        return Agent(config=self.agent_config['stock_picker'])
    
    @task
    def find_trending_company(self) -> Task:
        return Task(
            config=self.tasks_config['research_trending_companies'],
            output_pydantic=TrendingCompanyResearchList
        )

    @task
    def pick_best_company(self) -> Task:
        return Task(
            config=self.tasks_config['pick_best_company']
        )

    @crew
    def crew(self) -> Crew:
        manager = Agent(
            config=self.agent_config['manager'],
            allow_delegation=True
        )
        return Crew(
            agents=self.agents,
            task=self.tasks,
            process=Process.hierarchical,
            verbose=True,
            manager_agent=manager
        )    
    
    