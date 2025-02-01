"""
This example shows how using a decorator to manage dependencies
allows for easy changes without modifying the class internals.

But using a decorator seems to be overengineered
because we can use a simpler code:
```python
service = NotificationService()
service.sender = SmsSender()
```

An issue is opened for this:
https://github.com/PacktPublishing/Mastering-Python-Design-Patterns-Third-Edition/issues/9

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


def inject_sender(sender_cls):
	def decorator(cls):  # `cls` will be `NotificationService`
		cls.sender = sender_cls()
		return cls
	return decorator


# decorator
@inject_sender(EmailSender)
class NotificationService:
	sender: NotificationSender = None

	def notify(self, message):
		self.sender.send(message)


if __name__ == "__main__":
	email_service = NotificationService()  # The class got `EmailSender` as `sender` via the decorator
	email_service.notify("Hello, this is a test notification!")
	# Sending Email: Hello, this is a test notification!

	# Implicitly apply the decorator with another parameter to change the `NotificationService`'s `sender` attribute
	sms_service = inject_sender(SmsSender)(NotificationService)()
	sms_service.notify("Hello, this is a test notification!")
	# Sending SMS: Hello, this is a test notification!
