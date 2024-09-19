
from anthropic import Anthropic
import os
from dotenv import load_dotenv


load_dotenv()
my_api_key = os.getenv("ANTHROPIC_API_KEY")

# Initialize the Anthropic client
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Initialize conversation history
conversation_history = []

print("Start chatting with the AI assistant. Type 'quit' to end the conversation.")

while True:
    user_input = input("User: ")

    if user_input.lower() == "quit":
        print("Conversation ended.")
        break

    conversation_history.append({"role": "user", "content": user_input})

    response = client.messages.create(
        model="claude-3-haiku-20240307",
        messages=conversation_history,
        max_tokens=500
    )

    assistant_response = response.content[0].text
    print(f"Assistant: {assistant_response}")
    conversation_history.append({"role": "assistant", "content": assistant_response})
