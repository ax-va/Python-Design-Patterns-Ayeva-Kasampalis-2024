# MessageService is loosely coupled with EmailSender and SMSSender through dependency injection.
# We can easily switch between different sending mechanisms without modifying the MessageService class.
class MessageService:
    def __init__(self, sender):
        # A dependency is injected via "sender"
        self.sender = sender

    def send_message(self, message):
        self.sender.send(message)


class EmailSender:
    def send(self, message):
        print(f"Sending email: {message}")


class SMSSender:
    def send(self, message):
        print(f"Sending SMS: {message}")


if __name__ == "__main__":
    email_service = MessageService(EmailSender())
    email_service.send_message("Hello via Email")
    # Sending email: Hello via Email

    sms_service = MessageService(SMSSender())
    sms_service.send_message("Hello via SMS")
    # Sending SMS: Hello via SMS
