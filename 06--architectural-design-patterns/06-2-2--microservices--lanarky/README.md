# Architectural Desing Patterns

## Microservices

The *Microservice Architecture* pattern, or *Microservices*, is used to build
an application as a set of loosely coupled, collaborating services.
These services are loosely coupled, independently deployable, and communicate via well-defined APIs.
We usually run those services packed as containers with our application server,
dependencies and runtime libraries, compiled code, configurations, etc.

## Example: an LLM service using Lanarky

- Lanarky is a web framework that builds upon the FastAPI framework 
to provide batteries for building Microservices that use *large language models (LLMs)*:

https://pypi.org/project/lanarky/
https://snyk.io/advisor/python/lanarky

- Install Lanarky and its dependencies:
```unix
$ python -m pip install lanarky uvicorn dotenv
```

- Visit https://platform.openai.com/account/api-keys and create an API key.
Store the secret key in `.env`:

```env
open_api_key=<your_key>
```

and add `.env` into `.gitignore`:

```
**/.env
```