import uvicorn
from dotenv import load_dotenv
from lanarky import Lanarky
from lanarky.adapters.openai.resources import ChatCompletionResource
from lanarky.adapters.openai.routing import OpenAIAPIRouter

# Store the secret OpenAPI key as the environment `OPEN_API_KEY` variable.
# The key is given in `.env` which is added to `.gitignore`.
# See `README.md` for more information.
load_dotenv()