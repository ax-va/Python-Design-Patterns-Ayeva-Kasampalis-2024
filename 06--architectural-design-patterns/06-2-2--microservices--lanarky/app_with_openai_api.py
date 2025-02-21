import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from `.env` file
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

while True:
    message = input()
    if message.lower() in ["exit", "quit", "stop", "ende"]:
        break

    # Define the chat messages
    messages = [
        {"role": "system", "content": "Here is your assistant."},
        {"role": "user", "content": message},
    ]

    try:
        # Create a chat completion
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
        )
    except Exception as e:
        print(e)
    else:
        # Extract and print the assistant's message
        assistant_message = response.choices[0].message.content
        print(assistant_message)
