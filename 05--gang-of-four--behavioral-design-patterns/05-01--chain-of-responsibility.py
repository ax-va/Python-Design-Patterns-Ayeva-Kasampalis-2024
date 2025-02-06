"""
Explanation of the UML class diagram for a UI event-based system:

1. Classes:
- `Widget` (base class)
- `Event`
- `MainWindow`, `MsgText`, `SendDialog` (derived classes from `Widget`)

2. Relationships:
- Inheritance (triangle arrowhead)
`MainWindow`, `MsgText`, and `SendDialog` inherit from `Widget`.

- Association (arrow)
`Event` is associated with `Widget`, meaning `Widget` handles `Event` objects.

- `Aggregation` (diamond symbol)
`Widget` has a parent-child relationship with itself,
meaning a `Widget` instance can consist of other `Widget` instances.

See also:
- https://legacy.python.org/workshops/1997-10/proceedings/savikko.html
- 4 Chain of Responsibility
"""


class Event:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name


class Widget:
	def __init__(self, parent=None):
		self.parent = parent

	def handle(self, event):
		handler = f"handle_{event}"
		if hasattr(self, handler):
			method = getattr(self, handler)
			method(event)
		elif self.parent is not None:
			self.parent.handle(event)
		elif hasattr(self, "handle_default"):
			self.handle_default(event)


# `MainWindow` can handle only the close and default events
class MainWindow(Widget):
	def handle_close(self, event):
		print(f"MainWindow: '{event}'")

	def handle_default(self, event):
		print(f"MainWindow Default: '{event}'")


# `SendDialog` can handle only the `paint` event
class SendDialog(Widget):
	def handle_paint(self, event):
		print(f"SendDialog: '{event}'")


# `MsgText` can handle only the `down` event
class MsgText(Widget):
	def handle_down(self, event):
		print(f"MsgText: '{event}'")


if __name__ == "__main__":
	main_window = MainWindow()
	send_dialog = SendDialog(main_window)
	msg_text = MsgText(send_dialog)

	for widget in (main_window, send_dialog, msg_text):
		for evt_name in ("down", "paint", "unhandled", "close"):
			evt = Event(evt_name)
			# Send an event to a widget
			print(f"Sending '{evt}' to {widget.__class__.__name__}...")
			widget.handle(evt)

# Sending 'down' to MainWindow...
# MainWindow Default: 'down'
# Sending 'paint' to MainWindow...
# MainWindow Default: 'paint'
# Sending 'unhandled' to MainWindow...
# MainWindow Default: 'unhandled'
# Sending 'close' to MainWindow...
# MainWindow: 'close'

# Sending 'down' to SendDialog...
# MainWindow Default: 'down'
# Sending 'paint' to SendDialog...
# SendDialog: 'paint'
# Sending 'unhandled' to SendDialog...
# MainWindow Default: 'unhandled'
# Sending 'close' to SendDialog...
# MainWindow: 'close'

# Sending 'down' to MsgText...
# MsgText: 'down'
# Sending 'paint' to MsgText...
# SendDialog: 'paint'
# Sending 'unhandled' to MsgText...
# MainWindow Default: 'unhandled'
# Sending 'close' to MsgText...
# MainWindow: 'close'
