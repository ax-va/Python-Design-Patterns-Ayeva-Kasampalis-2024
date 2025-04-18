"""
*Encapsulate what varies* =
Isolate the parts of your code that are most likely to change and encapsulate them.

- Advantages:
  - Ease of maintenance:      Reduce the risk of introducing bugs when only modifying the encapsulated parts
  - Enhanced flexibility:     Provide a more adaptable architecture when changing encapsulated components
  - Improved readability:     Code becomes more organized and easier to understand


- Polymorphism and properties:

  - *Polymorphism* allows instances of different classes to be treated as instances of a common superclass.
  - When using *properties*, *getters* allow reading the values of attributes and *setters* enable modifying them.
"""


class PaymentBase:
    def __init__(self, amount: int):
        self.amount: int = amount

    # Lets us know that each inherited class should implement this method for itself
    def process_payment(self):
        pass


class CreditCard(PaymentBase):
    # Encapsulated implementation
    def process_payment(self):
        msg = f"Credit card payment: {self.amount}"
        print(msg)


class PayPal(PaymentBase):
    # Encapsulated implementation
    def process_payment(self):
        msg = f"PayPal payment: {self.amount}"
        print(msg)


if __name__ == "__main__":
    payments = [CreditCard(100), PayPal(200)]
    for payment in payments:
        payment.process_payment()
# Credit card payment: 100
# PayPal payment: 200
