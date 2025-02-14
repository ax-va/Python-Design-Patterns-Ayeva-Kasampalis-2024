"""
The *memento* pattern is used to take a snapshot of the internal state of an object,
so that the object can be restored with it when needed.
In this design pattern, the following definitions are used:
- The *memento* is a simple object that contains basic state storage and retrieval capabilities.
- The *originator* is an object that gets and sets values of memento instances.
- The *caretaker* is an object that can store and retrieve all previously created memento instances.
"""