"""
The proxy design pattern contains:

- a *virtual proxy*, which uses *lazy initialization* to defer
the creation of a computationally expensive object until the moment it is actually needed;

- a *protection/protective proxy*, which controls access to a sensitive object;

- a *remote proxy*, which acts as the local representation of an object that really exists
in a different address space (for example, a network server); an example: an object-relational mapping (ORM) API;

- a *smart (reference) proxy*, which performs extra actions when an object is accessed;
examples: reference counting and thread-safety checks.
"""
from abc import ABC, abstractmethod


# interface
class RemoteServiceInterface(ABC):
	@abstractmethod
	def read_file(self, filename):
		pass

	@abstractmethod
	def write_file(self, filename, contents):
		pass

	@abstractmethod
	def delete_file(self, filename):
		pass


# The file handling on the remote service is
# simplified in this an interface implementation.
class RemoteService(RemoteServiceInterface):
	def read_file(self, filename):
		# Implementation for reading a file from the server
		return "Reading file from remote server."

	def write_file(self, filename, contents):
		# Implementation for writing to a file on the server
		return "Writing to file on remote server."

	def delete_file(self, filename):
		# Implementation for deleting a file from the server
		return "Deleting file from remote server."


# The Proxy handles the communication with the remote service,
# (potentially adding logging, access control, or caching).
class ProxyService(RemoteServiceInterface):
	def __init__(self):
		self.remote_service = RemoteService()

	def read_file(self, filename):
		print("Proxy: Forwarding read request to `RemoteService`.")
		return self.remote_service.read_file(filename)

	def write_file(self, filename, contents):
		print("Proxy: Forwarding write request to `RemoteService`.")
		return self.remote_service.write_file(filename, contents)

	def delete_file(self, filename):
		print("Proxy: Forwarding delete request to `RemoteService`.")
		return self.remote_service.delete_file(filename)


# Clients interact with the `ProxyService` component,
# unaware of the remote nature of the actual service.
if __name__ == "__main__":
	proxy = ProxyService()
	print(proxy.read_file("example.txt"))
	# Proxy: Forwarding read request to `RemoteService`.
	# Reading file from remote server.
