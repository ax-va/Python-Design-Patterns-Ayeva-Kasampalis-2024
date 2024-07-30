"""
Program to Interfaces, Not Implementations
= Code against an interface rather than a concrete class.

Benefits:
- Flexibility:          Easily switch between different implementations without altering the code that uses them
- Maintainability:      Make the code easier to update or replace components because of no specific implementations
- Testability:          Simpler to write unit tests, as you can easily mock the interface during testing

In Python, interfaces can be implemented using two primary techniques:

1. abstract base classes (ABCs)
->
Define abstract methods that must be implemented by any concrete (i.e., non-abstract) subclass.

2. protocols
->
Offer a more flexible approach than ABCs, known as *structural duck typing*,
where an object is considered valid if it has certain attributes or methods,
regardless of its actual inheritance.
"""
from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass


class ConsoleLogger(Logger):
    def log(self, message: str):
        print(f"Console: {message}")


class FileLogger(Logger):
    def log(self, message: str):
        with open("log.txt", "a") as f:
            f.write(f"File: {message}\n")


def log_message(logger: Logger, message: str):
    logger.log(message)


if __name__ == "__main__":
    log_message(ConsoleLogger(), "A console log.")
    log_message(FileLogger(), "A file log.")
