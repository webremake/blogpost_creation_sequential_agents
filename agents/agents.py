import asyncio
from dotenv import load_dotenv

load_dotenv()

GEMINI_MODEL_NAME = "gemini-2.5-flash-lite"
RESEARCH_FINDINGS_KEY = "research_findings"
FINAL_SUMMARY_KEY = "final_summary"

# pip install google-adk

# Import ADK components
from google.adk.agents import Agent, SequentialAgent, ParallelAgent, LoopAgent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner
from google.adk.tools import AgentTool, FunctionTool, google_search
from google.genai import types

print("✅ ADK components imported successfully.")


# Configure retry options
retry_config = types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504], # Retry on these HTTP errors
)

gemini_model = Gemini(
    model=GEMINI_MODEL_NAME,
    retry_options=retry_config
)

# Research Agent: Its job is to use the google_search tool and present findings.
research_agent = Agent(
    name="ResearchAgent",
    model=gemini_model,
    instruction="""You are a specialized research agent. Your only job is to use the
    google_search tool to find 2-3 pieces of relevant information on the given topic and present the findings with citations.""",
    tools=[google_search],
    output_key=RESEARCH_FINDINGS_KEY,  # The result of this agent will be stored in the session state with this key.
)

print("✅ research_agent created.")


# Summarizer Agent: Its job is to summarize the text it receives.
summarizer_agent = Agent(
    name="SummarizerAgent",
    model=gemini_model,
    # The instruction is modified to request a bulleted list for a clear output format.
    instruction=f"""Read the provided research findings: {{{RESEARCH_FINDINGS_KEY}}}
Create a concise summary as a bulleted list with 3-5 key points.""",
    output_key=FINAL_SUMMARY_KEY,
)

print("✅ summarizer_agent created.")


# Root Coordinator: Orchestrates the workflow by calling the sub-agents as tools.
root_agent = Agent(
    name="ResearchCoordinator",
    model=gemini_model,
    # This instruction tells the root agent HOW to use its tools (which are the other agents).
    instruction="""You are a research coordinator. Your goal is to answer the user's query by orchestrating a workflow.
1. First, you MUST call the `ResearchAgent` tool to find relevant information on the topic provided by the user.
2. Next, after receiving the research findings, you MUST call the `SummarizerAgent` tool to create a concise summary.
3. Finally, present the final summary clearly to the user as your response.
    Всегда отвечай  на языке на котором задан вопрос.""",
    # We wrap the sub-agents in `AgentTool` to make them callable tools for the root agent.
    tools=[AgentTool(research_agent), AgentTool(summarizer_agent)],
)

print("✅ root_agent created.")

async def main():
    """
    Асинхронная функция для запуска агентов.
    """
    print("🚀 Starting agent execution...")
    runner = InMemoryRunner(agent=root_agent, app_name="agents")
    
    # Используем await внутри async-функции
    events = await runner.run_debug(
        "What is the difference between google и Yandex?.",
        quiet=True
    )
    
    final_response_text = ""
    for event in reversed(events):
        if event.content and event.content.parts and event.content.parts[0].text and event.content.role == 'model':
            final_response_text = event.content.parts[0].text
            break
    
    print("\n--- Final Result ---")
    print(final_response_text)

if __name__ == "__main__":
    # Запускаем асинхронную функцию main
    asyncio.run(main())

