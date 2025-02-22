from lanarky.clients import StreamingClient

client = StreamingClient()

while True:
	message = input()
	if message.lower() in ["exit", "quit", "stop"]:
		break

	for event in client.stream_response(
		"POST",
		"/chat",
		params={"stream": "false"},
		json={"messages": [{"role": "user", "content": message}]}
	):
		print(f"{event.event}: {event.data}")


"""
Hallo!
completion: Hallo! Wie kann ich Ihnen helfen?
"""
