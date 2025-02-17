"""
The *Model-View-Controller (MVC)* pattern is an application of the *separation of concern* principle and
used for *loose coupling* to split a software application into three components:

- The *model* is the core component that contains and manages
the (business) logic, data, state, and rules of an application.

- The *view* is a visual representation of the model to only displays the data (but not to handle it).
The examples may be a GUI, an output in a terminal, a PDF document, a chart, and so forth.

- The *controller* is used for all communication between the model and the view.
The controller allows us to use more than one view without modifying the model.
To achieve decoupling between the model and its representation, every view typically needs its own controller.

When implementing MVC from scratch, be sure that you create smart models, thin controllers, and dumb views.
"""

# Example: The user enters a number and sees the quote related to that number

quotes = (
	"A man is not complete until he is married. Then he is finished.",
	"As I said before, I never repeat myself.",
	"Facts are stubborn things.",
)


class QuoteModel:
	def get_quote(self, n):
		try:
			value = quotes[n]
		except IndexError as err:
			value = "Not found!"
		return value


class QuoteTerminalView:
	def show(self, quote):
		print(f'And the quote is: "{quote}"')

	def error(self, msg):
		print(f"Error: {msg}")

	def select_quote(self):
		return input("Which quote number would you like to see? ")


class QuoteTerminalController:
	def __init__(self):
		self.model = QuoteModel()
		self.view = QuoteTerminalView()

	def run(self):
		valid_input = False
		while not valid_input:
			n = self.view.select_quote()
			try:
				n = int(n)
			except ValueError:
				self.view.error(f"Incorrect index '{n}'")
			valid_input = True
			quote = self.model.get_quote(n)
			self.view.show(quote)


def main():
	controller = QuoteTerminalController()
	while True:
		controller.run()


if __name__ == "__main__":
	main()
	"""
	Which quote number would you like to see? 1
	And the quote is: "As I said before, I never repeat myself."
	Which quote number would you like to see? 10
	And the quote is: "Not found!"
	Which quote number would you like to see? 0
	And the quote is: "A man is not complete until he is married. Then he is finished."
	Which quote number would you like to see? exit()
	Error: Incorrect index 'exit()'
	"""
