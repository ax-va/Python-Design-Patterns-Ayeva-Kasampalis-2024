# Architectural Desing Patterns

## Microservices

### Example: an LLM service using Lanarky

- Lanarky is a web framework that builds upon the FastAPI framework 
to provide batteries for building Microservices that use *large language models (LLMs)*:

https://pypi.org/project/lanarky/

https://snyk.io/advisor/python/lanarky

- Install Lanarky with its dependencies and other packages.
Lanarky 0.8.8 does not support Python 3.12+. 
Make sure that your virtual environment is build with Python 3.11 to install Lanarky in this case.
```unix
$ python -m pip install lanarky[openai]==0.8.8 uvicorn dotenv
```

- Visit https://platform.openai.com/account/api-keys and create an API key.
Store the secret key in `.env`:

```env
OPENAI_API_KEY=<your_key>
```

and add `.env` into `.gitignore`:

```
**/.env
```
- To experiment with the OpenAI API, I paid $5.95 one-time.
