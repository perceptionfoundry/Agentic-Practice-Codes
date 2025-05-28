from agents import Agent, WebSearchTool, ModelSettings

INSTRUCTION = (
    "You are research assistant, Given a search term, you search the web for that term and"
    "produce a concise summary of the results. The summary must 2-3 paragraphs and less than 300"
    "words, Capture the main points. Write succiently, no need to have complete sentences of goods"
    "grammer. This will be consumed by someone synthesizing a report, so its vital you capture the"
    "essence and ignore any fluff. Do not include any additional commentary othe than the summary itself"
    )

search_agent = Agent(
    name="Search agent",
    instructions=INSTRUCTION,
    tools=[WebSearchTool(search_context_size="low")],
    model="gpt-4o-mini",
    model_settings=ModelSettings(tool_choice="required")
)