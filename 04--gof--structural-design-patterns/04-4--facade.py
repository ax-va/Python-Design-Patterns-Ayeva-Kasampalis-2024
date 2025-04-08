"""
Facade

The *Facade* pattern is for providing a simple interface to client code
that wants to use a complex system but does not need to be aware of the system's complexity.
We can hide the internal complexity of our systems and expose only
what is necessary to the client through a simplified interface.
"""
from abc import ABC, abstractmethod
from enum import Enum

# Example: a multi-server operating system consisting of the *microkernel*
# and servers such as a file server, a process server, an authentication server,
# a network server, a graphical/window server, and so forth.

State = Enum(
    "State",
    "NEW RUNNING SLEEPING RESTART ZOMBIE",
)

# complex system (consisting of an abstract server class and two stub server subclasses)

class Server(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def __str__(self):
        return self.name

    @abstractmethod
    def boot(self):
        pass

    @abstractmethod
    def kill(self, restart=True):
        pass


class FileServer(Server):
    def __init__(self):
        self.name = "FileServer"
        self.state = State.NEW

    def boot(self):
        print(f"Booting {self}")
        self.state = State.RUNNING

    def kill(self, restart=True):
        print(f"Killing {self}")
        self.state = State.RESTART if restart else State.ZOMBIE

    def create_file(self, user, name, perms):
        msg = (
            f"Trying to create file '{name}' "
            f"for user '{user}' "
            f"with permissions {perms}"
        )
        print(msg)


class ProcessServer(Server):
    def __init__(self):
        self.name = "ProcessServer"
        self.state = State.NEW

    def boot(self):
        print(f"Booting {self}")
        self.state = State.RUNNING

    def kill(self, restart=True):
        print(f"Killing {self}")
        self.state = State.RESTART if restart else State.ZOMBIE

    def create_process(self, user, name):
        msg = (
            f"Trying to create process '{name}' "
            f"for user '{user}'"
        )
        print(msg)


# The OperatingSystem class is a facade
class OperatingSystem:
    """ The Facade """

    def __init__(self):
        self.fs = FileServer()
        self.ps = ProcessServer()

    def start(self):
        """ The entry point to the system (used by the client code) """
        for server in [self.fs, self.ps]:
            server.boot()

    def create_file(self, user, name, perms):
        """ A wrapper method """
        return self.fs.create_file(user, name, perms)

    def create_process(self, user, name):
        """ A wrapper method """
        return self.ps.create_process(user, name)


def main():
    # The client code interacts only with the facade instance
    # and doesn't need to know internal details about the operating system,
    # such as the existence of multiple servers.
    os = OperatingSystem()
    os.start()
    os.create_file("foo", "hello.txt", "-rw-r-r")
    os.create_process("bar", "ls /tmp")


if __name__ == "__main__":
    main()
    # Booting FileServer
    # Booting ProcessServer
    # Trying to create file 'hello.txt' for user 'foo' with permissions -rw-r-r
    # Trying to create process 'ls /tmp' for user 'bar'
