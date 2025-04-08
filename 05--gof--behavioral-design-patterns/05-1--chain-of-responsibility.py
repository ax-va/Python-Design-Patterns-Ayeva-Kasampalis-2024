"""
Chain of Responsibility

The *Chain of Responsibility* pattern is used to handle requests by passing them from the sender (client) to receivers
(processing elements, handlers) through a chain of handlers.
Each handler decides either whether it can process the request or whether it should delegate it further along the chain.
The client only interacts with the first processing element in the chain,
the first one with only the second one, and so on.
Thus, the client only needs to know how to communicate with the start (head) of the chain.

Explanation of the UML class diagram for a GUI event-based system:

1. Classes:
- `Widget` (base class)
- `Event`
- `MainWindow`, `MsgText`, `SendDialog` (inheriting classes from `Widget`)

2. Relationships:
- Inheritance (triangle arrowhead from the inheriting classes to `Widget`)
`MainWindow`, `MsgText`, and `SendDialog` inherit from `Widget`.

- Association (simple arrow from `Widget` to `Event`)
`Event` is associated with `Widget`, meaning `Widget` handles `Event` objects.

- `Aggregation` (diamond symbol at `Widget` linked to `Widget` by line)
`Widget` has a parent-child relationship with itself,
meaning a `Widget` instance can contain / consist of other `Widget` instances.

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
        for event_name in ("down", "paint", "unhandled", "close"):
            event = Event(event_name)
            # Send an event to a widget
            print(f"Sending '{event}' to {widget.__class__.__name__}...")
            widget.handle(event)

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
