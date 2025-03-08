"""
Proxy

The Proxy design pattern contains:

- a *virtual proxy*, which uses *lazy initialization* to defer
the creation of a computationally expensive object until the moment it is actually needed;

- a *protection/protective proxy*, which controls access to a sensitive object;

- a *remote proxy*, which acts as the local representation of an object that really exists
in a different address space (for example, a network server); an example: an object-relational mapping (ORM) API;

- a *smart (reference) proxy*, which performs extra actions when an object is accessed;
examples: reference counting and thread-safety checks.
"""

from abc import ABC, abstractmethod

# Example:
# a simple protection proxy to view and add users with two options:
# - view the list of users that *does not* require special privileges,
# - add a new user that requires the client to provide a special secret message.

# This abstract class contains the information that we want to protect
class SensitiveInfo(ABC):
	def __init__(self):
		self.users = ["nick", "tom", "ben", "mike"]

	@abstractmethod
	def read(self):
		pass

	@abstractmethod
	def add(self, user):
		pass


# "Private" concrete class that actually implements `SensitiveInfo`
class _ConcreteSensitiveInfo(SensitiveInfo):
	def read(self):
		num = len(self.users)
		print(f"There are {num} users: {', '.join(self.users)}.")

	def add(self, user):
		self.users.append(user)
		print(f"Added user '{user}'.")


# This class is a protection proxy of `_ConcreteSensitiveInfo`
class Info:
	def __init__(self):
		self.protected = _ConcreteSensitiveInfo()
		# Notation: in reality, *never*
		# - store passwords in the source code,
		# - store passwords in clear-text form,
		# - use a weak (for example, MD5) or custom form of encryption.
		self.secret = "0xdeadbeef"

	def read(self):
		self.protected.read()

	def add(self, user):
		secret = input("Input the secret: ")
		if secret == self.secret:
			self.protected.add(user)
		else:
			print("That's wrong!")


# How to use the proxy pattern in the client code
def main():
	info = Info()  # proxy instance
	while True:
		print("1 = read list\n2 = add user\n3 = quit")
		option_key = input("Input option: ")
		if option_key == "1":
			info.read()
		elif option_key == "2":
			user = input("Input user: ")
			info.add(user)
		elif option_key == "3":
			exit()
		else:
			print(f"Unknown option: {option_key}")


if __name__ == "__main__":
	main()
