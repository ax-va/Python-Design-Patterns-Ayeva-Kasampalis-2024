import unittest

from notifications import (
	NotificationSender,
	NotificationService,
	inject_sender,
)


# Two stub classes implement the `NotificationSender` interface

class EmailSenderStub:
	def __init__(self):
		self.messages_sent = []

	def send(self, message: str):
		self.messages_sent.append(message)


class SmsSenderStub:
	def __init__(self):
		self.messages_sent = []

	def send(self, message: str):
		self.messages_sent.append(message)


class TestNotifService(unittest.TestCase):
	def test_notify_with_email(self):
		email_stub = EmailSenderStub()
		service = NotificationService()
		# Overwrite `sender`
		service.sender = email_stub
		service.notify("Test Email Message")
		self.assertIn(
			"Test Email Message",
			email_stub.messages_sent,
		)


	def test_notify_with_sms(self):
		sms_stub = SmsSenderStub()
		# What's the point of a decorator
		# if the `sender` method still needs to be overwritten?
		service = inject_sender(SmsSenderStub)(NotificationService)()
		# Overwrite `service.sender` because `sms_stub` and `service.sender`
		# are different instances of `SmsSenderStub`.
		service.sender = sms_stub
		service.notify("Test SMS Message")
		self.assertIn(
			"Test SMS Message",
			sms_stub.messages_sent
		)


if __name__ == "__main__":
	unittest.main()
	# ...
	# Ran 1 test in 0.002s
	#
	# OK
	# ...
