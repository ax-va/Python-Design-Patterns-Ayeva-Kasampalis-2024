import uvicorn
from dotenv import load_dotenv
from lanarky import Lanarky
from lanarky.adapters.openai.resources import ChatCompletionResource
from lanarky.adapters.openai.routing import OpenAIAPIRouter

# Store the secret OpenAPI key as the environment variable `OPEN_API_KEY`.
# The key is given in `.env` which is added to `.gitignore`.
load_dotenv()

# # Check whether the secret key is stored as the environment variable
# import os
# print(os.getenv["OPENAI_API_KEY"])

app = Lanarky()
router = OpenAIAPIRouter()


@router.post("/chat")
def chat(stream: bool = True) -> ChatCompletionResource:
	system = "Here is your assistant"
	return ChatCompletionResource(
		model="gpt-4o",
		stream=stream,
		system=system,
	)


if __name__ == "__main__":
	app.include_router(router)
	uvicorn.run(app)

"""
$ python llm_service.py
INFO:     Started server process [32158]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:52312 - "POST /chat?stream=false HTTP/1.1" 200 OK
INFO:     127.0.0.1:52270 - "POST /chat?stream=false HTTP/1.1" 200 OK
INFO:     127.0.0.1:50882 - "POST /chat?stream=false HTTP/1.1" 200 OK
<CTRL + C>
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [32158]
"""
