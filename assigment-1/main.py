# agent.py
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel
import os
from dotenv import load_dotenv

load_dotenv()
client = AsyncOpenAI(api_key=os.getenv("GEMINI_API_KEY"))

MODEL = OpenAIChatCompletionsModel(model="gemini-1.5-flash", client=client)

agent = Agent(
    model=MODEL,
    name="Simple Assistant",
    instructions="You are a helpful assistant. Answer user queries clearly."
)

runner = Runner(agent)
