"""
The Proxy design pattern contains:

- a *virtual proxy*, which uses *lazy initialization* to defer
the creation of a computationally expensive object until the moment it is actually needed;

- a *protection/protective proxy*, which controls access to a sensitive object;

- a *remote proxy*, which acts as the local representation of an object that really exists
in a different address space (for example, a network server); an example: an object-relational mapping (ORM) API;

- a *smart (reference) proxy*, which performs extra actions when an object is accessed;
examples: reference counting and thread-safety checks.
"""
from typing import Protocol

# Example: a *smart proxy* for a shared resource, for instance, a database connection.
# The smart proxy manages the reference counting for this database connection and ensures
# that the resource is created on demand and only closed once all references to it are released.

class DBConnectionInterface(Protocol):
	def exec_query(self, query):
		...


class DBConnection:
	def __init__(self):
		print("DB connection created.")

	def exec_query(self, query):
		return f"Executing query: '{query}'."

	def close(self):
		print("DB connection closed.")


class SmartProxy:
	def __init__(self):
		self.conn = None
		self.ref_count = 0

	def access_resource(self):
		if self.conn is None:
			self.conn = DBConnection()
		self.ref_count += 1
		print(f"DB connection now has {self.ref_count} references.")

	def exec_query(self, query):
		if self.conn is None:
			# Ensure the connection is created if not already
			self.access_resource()
		result = self.conn.exec_query(query)
		print(result)

		# Decrement reference count after
		self.release_resource()

		return result

	def release_resource(self):
		if self.ref_count > 0:
			self.ref_count -= 1
			print("Reference released...")
			print(f"{self.ref_count} remaining references.")

		if self.ref_count == 0 and self.conn is not None:
			self.conn.close()
			self.conn = None


if __name__ == "__main__":
	proxy = SmartProxy()
	proxy.exec_query("SELECT * FROM users")
	# DB connection created.
	# DB connection now has 1 references.
	# Executing query: 'SELECT * FROM users'.
	# Reference released...
	# 0 remaining references.
	# DB connection closed.
	proxy.exec_query("UPDATE users SET name = 'John Doe' WHERE id = 1")
	# DB connection created.
	# DB connection now has 1 references.
	# Executing query: 'UPDATE users SET name = 'John Doe' WHERE id = 1'.
	# Reference released...
	# 0 remaining references.
	# DB connection closed.
