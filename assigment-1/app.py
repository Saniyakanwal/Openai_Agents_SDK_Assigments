import chainlit as cl
from agents import runner

@cl.on_chat_start
async def start_chat():
    await cl.Message(content="Hello 👋! Main tumhara AI Assistant hoon. Tum kya poochna chahte ho?").send()

@cl.on_message
async def handle_message(message: cl.Message):
    # run agent with user message
    run_result = await runner.run(message.content)

    # agent ka output text nikalna
    reply = ""
    if hasattr(run_result, "output_text"):
        reply = run_result.output_text
    elif hasattr(run_result, "messages"):
        # agar multiple messages hain to join kar lo
        reply = " ".join([m["content"] for m in run_result.messages if m["role"] == "assistant"])
    else:
        reply = str(run_result)

    # send response to Chainlit UI
    await cl.Message(content=reply).send()
