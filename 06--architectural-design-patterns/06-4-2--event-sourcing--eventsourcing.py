"""
The *Event Sourcing* pattern helps us in storing all changes to an application state as a sequence of events.
This way, the application state can be reconstructed at any point in time by replaying these events.

The components of the Event Sourcing pattern implementation are as follows:

- **Event**: A representation of a state change. Once an event is created and applied, it cannot be changed.

- **Aggregate**: An object (or group of objects) for tracking that represents a single unit of business logic or data.
Every time something changes (an event), it makes a record of it.

- **Event store**: A collection of all the events that have occurred.

See also:

- **eventsourcing**

	- https://pypi.org/project/eventsourcing/
	- https://github.com/pyeventsourcing/eventsourcing
	- https://snyk.io/advisor/python/eventsourcing

```unix
$ python -m pip install eventsourcing
```
"""
from eventsourcing.domain import Aggregate, event
from eventsourcing.application import Application

# Example:
# an inventory management system with tracking the quantity of items
# by using the eventsourcing package.

class InventoryItem(Aggregate):
	@event("ItemCreated")
	def __init__(self, name, quantity=0):
		self.name = name
		self.quantity = quantity

	@event("QuantityIncreased")
	def increase_quantity(self, amount):
		self.quantity += amount

	@event("QuantityDecreased")
	def decrease_quantity(self, amount):
		self.quantity -= amount


class InventoryApp(Application):
	def create_item(self, name, quantity):
		item = InventoryItem(name, quantity)
		# Collect pending events from given aggregates and
		# put them in the application's event store.
		self.save(item)
		return item.id

	def increase_item_quantity(self, item_id, amount):
		item = self.repository.get(item_id)
		item.increase_quantity(amount)
		self.save(item)

	def decrease_item_quantity(self, item_id, amount):
		item = self.repository.get(item_id)
		item.decrease_quantity(amount)
		self.save(item)


def main():
	app = InventoryApp()
	# Create a new item
	item_id = app.create_item("Laptop", 10)
	# Increase quantity
	app.increase_item_quantity(item_id, 5)
	# Decrease quantity
	app.decrease_item_quantity(item_id, 1)
	# Create a new item
	item_id = app.create_item("Mobile Phone", 20)
	# Increase quantity
	app.increase_item_quantity(item_id, 10)
	# Decrease quantity
	app.decrease_item_quantity(item_id, 5)

	notifs = app.notification_log.select(start=1, limit=5)
	notifs = [notif.state for notif in notifs]
	for notif in notifs:
		print(notif.decode())


if __name__ == "__main__":
	main()
	# {"timestamp":{"_type_":"datetime_iso","_data_":"2025-03-05T18:17:47.314864+00:00"},"originator_topic":"__main__:InventoryItem","name":"Laptop","quantity":10}
	# {"timestamp":{"_type_":"datetime_iso","_data_":"2025-03-05T18:17:47.315163+00:00"},"amount":5}
	# {"timestamp":{"_type_":"datetime_iso","_data_":"2025-03-05T18:17:47.315317+00:00"},"amount":1}
	# {"timestamp":{"_type_":"datetime_iso","_data_":"2025-03-05T18:17:47.315413+00:00"},"originator_topic":"__main__:InventoryItem","name":"Mobile Phone","quantity":20}
	# {"timestamp":{"_type_":"datetime_iso","_data_":"2025-03-05T18:17:47.315508+00:00"},"amount":10}
