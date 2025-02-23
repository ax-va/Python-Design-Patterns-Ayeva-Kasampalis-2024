import os
import openai
from dotenv import load_dotenv

# Load environment variables from `.env` file
load_dotenv()

# Initialize the OpenAI client
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError(
        "API key not found. "
        "Please ensure the `.env` file "
        "is correctly configured."
    )

client = openai.OpenAI(api_key=api_key)


def main():
    print(
        "Welcome to the chat! "
        "Type 'exit', 'quit', or 'stop' "
        "to end the conversation."
    )

    # Conversation history to maintain context
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        }
    ]

    try:
        while True:
            user_message = input("\nYou: ").strip()
            if not user_message:
                print("Please enter a message.")
                continue

            if user_message.lower() in ["exit", "quit", "stop"]:
                print("Chat ended. Goodbye!")
                break

            # Add user message to conversation history
            messages.append(
                {
                    "role": "user",
                    "content": user_message
                }
            )

            try:
                # Create a chat completion
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=messages,
                    temperature=0.7,
                    max_tokens=500
                )

                assistant_message = response.choices[0].message.content
                print(f"Assistant: {assistant_message}")

                # Add assistant response to conversation history
                messages.append(
                    {
                        "role": "assistant",
                        "content": assistant_message
                    }
                )

            except openai.OpenAIError as e:
                print(f"Error during API request: {e}")

    except KeyboardInterrupt:
        print("\nChat interrupted by user. Goodbye!")


if __name__ == "__main__":
    main()