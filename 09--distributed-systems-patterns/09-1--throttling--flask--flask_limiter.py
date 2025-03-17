"""
Throttling

The *Throttling* pattern is intended to control the rate of requests
a user (or a client service) can send to a given service or API in a given amount of time,
to protect the resources of the service from being overused.

Some examples of throttling:
- *Rate-Limit*,
- *IP-level Limit* (based on a list of whitelisted IP addresses, for example),
- *Concurrent Connections Limit*

Consider the following example: rate-limit-type throttling
by using Flask and its Flask-Limiter extension.

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


app = Flask(__name__)

limiter = Limiter(
	get_remote_address,
	app=app,
	# Restrict each client to no more than 100 requests per day
	# *and* no more than 10 requests per hour.
	default_limits=["100 per day", "10 per hour"],
	storage_uri="memory://",
	strategy="fixed-window",
)

@app.route("/limited")
def limited_api():
	return "This is a limited API."


@app.route("/more_limited")
@limiter.limit("2/minute")  # two requests per minute
def more_limited_api():
	return "This is a more limited API."


if __name__ == "__main__":
	app.run(debug=True)
	"""
	Open `http://127.0.0.1:5000/limited` and refresh the page 10 times per hour 
	to see on the page
	```
	Too Many Requests
	10 per 1 hour
	```
	and in the console
	```
	...
	127.0.0.1 - - [17/Mar/2025 21:19:00] "GET /limited HTTP/1.1" 200 -
	127.0.0.1 - - [17/Mar/2025 21:19:03] "GET /limited HTTP/1.1" 200 -
	127.0.0.1 - - [17/Mar/2025 21:19:04] "GET /limited HTTP/1.1" 200 -
	127.0.0.1 - - [17/Mar/2025 21:19:05] "GET /limited HTTP/1.1" 200 -
	127.0.0.1 - - [17/Mar/2025 21:19:05] "GET /limited HTTP/1.1" 200 -
	127.0.0.1 - - [17/Mar/2025 21:19:06] "GET /limited HTTP/1.1" 200 -
	127.0.0.1 - - [17/Mar/2025 21:19:07] "GET /limited HTTP/1.1" 200 -
	127.0.0.1 - - [17/Mar/2025 21:19:07] "GET /limited HTTP/1.1" 200 -
	127.0.0.1 - - [17/Mar/2025 21:19:08] "GET /limited HTTP/1.1" 200 -
	127.0.0.1 - - [17/Mar/2025 21:19:09] "GET /limited HTTP/1.1" 200 -
	127.0.0.1 - - [17/Mar/2025 21:19:09] "GET /limited HTTP/1.1" 429 -
	```
	Open `http://127.0.0.1:5000/more_limited` and refresh the page 2 times per minute 
	to see on the page
	```
	Too Many Requests
	2 per 1 minute
	```
	and in the console
	```
	...
	127.0.0.1 - - [17/Mar/2025 21:20:53] "GET /more_limited HTTP/1.1" 200 -
	127.0.0.1 - - [17/Mar/2025 21:20:55] "GET /more_limited HTTP/1.1" 200 -
	127.0.0.1 - - [17/Mar/2025 21:20:56] "GET /more_limited HTTP/1.1" 429 -
	```
	"""