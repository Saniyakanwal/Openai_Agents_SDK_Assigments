from agents import Agent,Runner,AsyncOpenAI, OpenAIChatCompletionsModel,set_tracing_disabled
from decouple import config
from Tools.math_tool import plus,multiply

set_tracing_disabled(True)

key = config("GEMINI_API_KEY")
base_url =config("GEMINI_BASE_URL") 

gemini_client = AsyncOpenAI(api_key= key, base_url= base_url)

Model = OpenAIChatCompletionsModel(model="gemini-1.5-flash",
openai_client= gemini_client)

agent = Agent(
    name = "Math Assistant",
    instructions = '''You are Math agent
    just perform plus or multiply function''',
    model = Model,
    tools=[plus,multiply]
)

if __name__ == "__main__":
    user_input = input("Enter your question: ")
    result = Runner.run_sync(agent, user_input) 
    print(result.final_output)
