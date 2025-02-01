"""
In this example, using a decorator seems to be overengineered.
"""
from typing import Protocol


class NotificationSender(Protocol):
	def send(self, message: str):
		"""Send a notification with the given message"""
		...


class EmailSender:
	def send(self, message: str):
		print(f"Sending Email: {message}")


class SmsSender:
	def send(self, message: str):
		print(f"Sending SMS: {message}")


# Do we need a decorator in this example?
def inject_sender(sender_cls):
	def decorator(cls):  # `cls` will be `NotificationService`
		cls.sender = sender_cls()
		return cls
	return decorator


@inject_sender(EmailSender)
class NotificationService:
	sender: NotificationSender = None

	def notify(self, message):
		self.sender.send(message)


if __name__ == "__main__":
	service = NotificationService()  # The class got `EmailSender` as `sender` via the decorator
	service.notify("Hello, this is a test notification!")
	# Sending Email: Hello, this is a test notification!

	# Isn't using a decorator overengineered?
	service.sender = SmsSender()
	service.notify("Hello, this is a test notification!")
	# Sending SMS: Hello, this is a test notification!
