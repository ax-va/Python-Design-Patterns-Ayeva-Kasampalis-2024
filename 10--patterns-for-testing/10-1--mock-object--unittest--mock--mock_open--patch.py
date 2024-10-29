"""
The *mock object* pattern serves to isolate components during testing by simulating their behavior.
It creates controlled testing environments and verifies interactions between components.

Three features of the mock object pattern:

1. isolation
->
Helps isolate the unit of code being tested, ensuring a controlled environment
for tests with predictable dependencies and no external side effects;

2. behavior verification
->
Helps verify that certain behaviors happen during a test, such as method calls or property accesses;

3. simplification:
->
Simplifies the setup of tests by replacing complex real objects that might require significant setup of their own.

Use cases:

- In *unit testing*, mock objects replace complex, unreliable, or unavailable dependencies of the code,
help focus solely on the unit itself rather than its interactions with external systems.
An example is mocking an API without needing to interact with the actual API,
when testing a service that fetches data from that.

- *Integration testing* with mock objects focuses on the interaction between components rather than individual units,
especially, to simulate components that have not been developed yet or are too costly to involve in every test.
An example is mocking in a microservices architecture, where a mock can represent a service that is under development or
temporarily unavailable, allowing other services to be tested in terms of how they integrate and communicate with it.

- In *behavior verification*, it can be verified with mock objects
whether certain interactions between objects occur as expected.
An example is testing whether a controller, in a Model View Controller (MVC) architecture,
correctly calls authentication and logging services before processing a user request, for instance,
to verify that the controller makes the right calls in the right order,
such as checking credentials before attempting to log the request.

## Features of `unittest.mock`

- Notice 1:
The `builtins` module provides direct access to all built-in identifiers of Python.
See also: https://docs.python.org/3/library/builtins.html

- Notice 2:
`mock_open()` returns a mock object that is configured to behave like the built-in `open` function.
The mock object is set up to simulate file operations such as reading and writing.
`mock_open` is also a callable object that behaves like a factory
for creating new mock file handles each time it's called.

- Notice 3:
The `unittest.mock.patch` context manager replace objects with mocks.
It includes a required arguments, `target`, to specify the object to replace, and
optional arguments: `new` to replace with it, and others.
See also: https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch
"""
import unittest
from unittest.mock import mock_open, patch

# Example: mocking the file-writing mechanism for logging

class Logger:
	""" Represents a simple logger to write messages to a file. """
	def __init__(self, filepath):
		self.filepath = filepath

	def log(self, message):
		with open(self.filepath, "a") as file:
			file.write(f"{message}\n")


class TestLogger(unittest.TestCase):
	def test_log(self):
		msg = "Hello, logging world!"
		# Mock the Python built-in `open` function by using `unittest.mock.patch`,
		# in the scope of which the target object, `builtins.open`, will be
		# temporarily replaced with a mock object, `mock_open()`.
		m_open = mock_open()
		with patch("builtins.open", m_open):
			logger = Logger("dummy.log")
			logger.log(msg)
			# Check whether the `open` function was called with the expected parameters
			m_open.assert_called_once_with("dummy.log", "a")
			# Obtain a new file handle by calling `m_open()`, and then use
			# `assert_called_once_with()` on the `write()` method call on that file handle
			# to check if the `write` method was called with the correct message.
			m_open().write.assert_called_once_with(f"{msg}\n")


if __name__ == "__main__":
	unittest.main()
