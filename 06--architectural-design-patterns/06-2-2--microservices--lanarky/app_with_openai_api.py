import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from `.env` file
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

while True:
    user_message = input()
    if user_message.lower() in ["exit", "quit", "stop"]:
        break

    # Define the chat messages
    messages = [
        {"role": "system", "content": "Here is your assistant."},
        {"role": "user", "content": user_message},
    ]

    try:
        # Create a chat completion
        response = client.chat.completions.create(
            model="gpt-4o-2024-11-20",
            messages=messages,
        )
    except Exception as e:
        print(e)
    else:
        # Extract and print the assistant's message
        assistant_message = response.choices[0].message.content
        print(assistant_message)
"""
Welches OpenAI Modell bist du?
Ich bin ein KI-Textmodell basierend auf OpenAI's GPT-4 Architektur. Mein Trainingsstand geht bis Oktober 2023. Wenn du Fragen hast, stehe ich dir gerne zur Verfügung! 😊
"""