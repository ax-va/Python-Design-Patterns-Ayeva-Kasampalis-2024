"""
*Loose coupling* =
Decrease the dependencies between different parts of a program so that
components are independent and interact through well-defined interfaces.

- Benefits:
  - Maintainability:          Easier to update or replace individual components because of fewer dependencies
  - Extensibility:            Can be more easily extended with new features or components
  - Testability:              Easier to test independent components in isolation


- There are two primary techniques to reduce the interdependencies between components:
    1. The **dependency injection** pattern allows a component to receive its dependencies from an external source
rather than creating them, making it easier to swap or mock these dependencies.

    2. The **observer** pattern allows an object to publish changes to its state so that other objects
can react accordingly, without being tightly bound to each other.
"""


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
