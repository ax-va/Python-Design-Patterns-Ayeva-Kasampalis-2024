"""
The adapter pattern is a structural design pattern to make two incompatible interfaces compatible.
For example, to adapt an old system component to a new system component or vice versa.

Consider: adapting a legacy class.
"""

# The legacy payment system uses a `make_payment` method
class OldPaymentSystem:
	def __init__(self, currency):
		self.currency = currency

	def make_payment(self, amount):
		print(f"[OLD] Pay {amount} {self.currency}")


# The new payment system uses an `execute_payment` method
class NewPaymentGateway:
	def __init__(self, currency):
		self.currency = currency

	def execute_payment(self, amount):
		print(f"Execute payment of {amount} {self.currency}")


# The `PaymentAdapter` class adapts the interface of `NewPaymentGateway` to match that of `OldPaymentSystem`
class PaymentAdapter:
	def __init__(self, system):
		self.system = system

	def make_payment(self, amount):
		self.system.execute_payment(amount)


def main():
	old_system = OldPaymentSystem("euro")
	print(old_system)
	new_system = NewPaymentGateway("euro")
	print(new_system)

	adapter = PaymentAdapter(new_system)
	adapter.make_payment(100)


if __name__ == "__main__":
	main()
	# <__main__.OldPaymentSystem object at 0x72dd43162900>
	# <__main__.NewPaymentGateway object at 0x72dd43162930>
	# Execute payment of 100 euro