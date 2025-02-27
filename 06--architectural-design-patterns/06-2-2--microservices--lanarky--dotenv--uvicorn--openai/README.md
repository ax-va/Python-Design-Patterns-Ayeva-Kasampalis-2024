# Architectural Desing Patterns

## Microservices

The *Microservice Architecture* pattern, or *Microservices*, is used to build 
an application as a set of loosely coupled, collaborating services.
These services are loosely coupled, independently deployable, and communicate via well-defined APIs.
We usually run those services packed as containers with our application server, 
dependencies and runtime libraries, compiled code, configurations, etc.

### Example: an LLM service using Lanarky

- Lanarky is a web framework that builds upon the FastAPI framework 
to provide batteries for building Microservices that use *large language models (LLMs)*:

  - https://pypi.org/project/lanarky/
  
  - https://snyk.io/advisor/python/lanarky


- Install Lanarky with its dependencies and other packages.
  Lanarky 0.8.8 does not support Python 3.12+. 
  Make sure that your virtual environment is build with Python 3.11 to install Lanarky.

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

- You must pay to work with OpenAI API. 
I paid $5.95 one-time to gain the simplest access to OpenAI models.


- Run `app_with_openai_api` and write a message to check whether the OpenAI API works as expected.


- In different terminals, first run the `llm_service` service and then the `client` client.