"""
*Dependency Inversion Principle* (DIP) =
High-level modules should not depend directly on low-level modules.
Instead, both should depend on abstractions or interfaces.

The DIP is closely linked to the *loose coupling* principle by promoting a design
where components interact through interfaces rather than concrete implementations.
"""


# - Anti-example with no DIP:
# The high-level Notification class is dependent on the low-level Email class.
class Email:
    """ Low-level class """
    def send_email(self, message):
        print(f"Sending email: {message}")


class Notification:
    """ High-level class """
    def __init__(self):
        self.email = Email()

    def send(self, message):
        self.email.send_email(message)


# - Example with DIP:
# Both Notification and Email are based on the # MessageSender abstraction.
from typing import Protocol


class MessageSender(Protocol):
    def send(self, message: str):
        ...


class Email:
    """ The low-level class implements the MessageSender interface. """
    def send(self, message: str):
        print(f"Sending email: {message}")


class Notification:
    """
    The high-level class also implements the MessageSender interface,
    and has an object that implements MessageSender.
    """
    def __init__(self, sender: MessageSender):
        self.sender: MessageSender = sender

    def send(self, message: str):
        self.sender.send(message)


if __name__ == "__main__":
    email = Email()
    notif = Notification(sender=email)
    notif.send(message="This is the message.")
    # Sending email: This is the message.
