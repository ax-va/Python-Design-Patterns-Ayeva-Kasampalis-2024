"""
This example of applying the Microservices pattern consists of a service and a client.
"""
from lanarky.clients import StreamingClient

client = StreamingClient()
messages = []

while True:
	user_message = input("\nYou: ").strip()
	if not user_message:
		print("Please enter a message.")
		continue

	if user_message.lower() in ["exit", "quit", "stop"]:
		print("Chat ended. Goodbye!")
		break

	# The LLM remembers what the user asked
	messages.append({"role": "user", "content": user_message})

	for event in client.stream_response(
		"POST",
		"/chat",
		params={"stream": "false"},
		json={"messages": messages}
	):
		assistant_message = event.data
		print(f"{event.event}: {assistant_message}")
		# The LLM remembers what it answered
		messages.append({"role": "assistant", "content": assistant_message})


"""
$ python client.py

You: Nenne mir eine Zahl 1 bis 9
completion: Natürlich, die Zahl ist 7.

You: Welche Zahl hast du mir gerade genannt?
completion: Die Zahl, die ich dir gerade genannt habe, war 7.

You:
"""
