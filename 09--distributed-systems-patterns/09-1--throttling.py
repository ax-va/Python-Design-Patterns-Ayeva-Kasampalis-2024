"""
Throttling

The *Throttling* pattern is intended to control the rate of requests
a user (or a client service) can send to a given service or API in a given amount of time,
to protect the resources of the service from being overused.

Example: throttling of the *Rate-Limit* type

See also:
- Flask
  - https://pypi.org/project/Flask/
  - https://github.com/pallets/flask/
  - https://snyk.io/advisor/python/flask
  ```
  $ pip install Flask
  ```
- Flask-Limiter
  - https://pypi.org/project/Flask-Limiter/
  - https://github.com/alisaifee/flask-limiter
  - https://snyk.io/advisor/python/flask-limiter
  ```
  $ pip install Flask-Limiter
  ```
"""
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

