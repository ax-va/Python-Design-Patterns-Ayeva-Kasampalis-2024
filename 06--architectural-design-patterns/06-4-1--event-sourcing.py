"""
Event Sourcing

The *Event Sourcing* pattern helps us in storing all changes to an application state as a sequence of events.
This way, the application state can be reconstructed at any point in time by replaying these events.

The components of the Event Sourcing pattern implementation are as follows:

- **Event**: A representation of a state change. Once an event is created and applied, it cannot be changed.

- **Aggregate**: An object (or group of objects) for tracking that represents a single unit of business logic or data.
Every time something changes (an event), it makes a record of it.

- **Event store**: A collection of all the events that have occurred.
"""

# Example: manual implementation of the Event Sourcing pattern for the bank account

# This class acts as the *aggregate*
class Account:
    def __init__(self):
        self.balance = 0
        # *event store*
        self.events = []

    def apply_event(self, event):
        event["balance_before"] = self.balance
        if event["type"] == "deposited":
            self.balance += event["amount"]
        elif event["type"] == "withdrawn":
            self.balance -= event["amount"]
        event["balance_after"] = self.balance
        self.events.append(event)

    def deposit(self, amount):
        event = {"type": "deposited", "amount": amount}
        self.apply_event(event)

    def withdraw(self, amount):
        event = {"type": "withdrawn", "amount": amount}
        self.apply_event(event)


def main():
    account = Account()
    account.deposit(100)
    account.deposit(50)
    account.withdraw(100)
    account.deposit(25)
    for event in account.events:
        print(event)


if __name__ == "__main__":
    main()
    # {'type': 'deposited', 'amount': 100, 'balance_before': 0, 'balance_after': 100}
    # {'type': 'deposited', 'amount': 50, 'balance_before': 100, 'balance_after': 150}
    # {'type': 'withdrawn', 'amount': 100, 'balance_before': 150, 'balance_after': 50}
    # {'type': 'deposited', 'amount': 25, 'balance_before': 50, 'balance_after': 75}
