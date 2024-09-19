# LLM_notes

- Understanding the messages API format
- understanding model response objects
- Build a simple multi-turn chatbot to run on the commandline

### creating a multi-turn command-line chatbot script:

This script creates a simple chat interface where you can have a conversation with Claude-3-Haiku. It maintains a conversation history, allowing the AI to remember and refer to previous parts of the conversation

1. Save it to a file, for example chat_with_claude.py.
2. Make sure you have the Anthropic Python library installed. You can install it using pip: pip install anthropic

3. Set your Anthropic API key as an environment variable. You can do this in your terminal before running the script:
(export ANTHROPIC_API_KEY=your_api_key_here)

4. Replace your_api_key_here with your actual Anthropic API key.
Run the script: python chat_with_claude.py

5. Start chatting with the AI assistant. Type your messages and press Enter. The assistant will respond to each of your inputs.
6. To end the conversation, type 'quit' and press Enter.
