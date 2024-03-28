import anthropic
from dotenv import load_dotenv
import os

load_dotenv()
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
input_message = [{"role": "user", "content": "hello!"}]
model = "claude-3-haiku-20240307"

with client.messages.stream(
    max_tokens=1024,
    messages=input_message,
    model=model,
) as stream:
    for event in stream:
        if event.type == "content_block_delta":
            print(event.delta.text)
        if event.type == "message_delta":
            print()
            print("output tokens:", event.usage.output_tokens)
    accumulated = stream.get_final_message()
    print("input tokens:", accumulated.usage.input_tokens)
