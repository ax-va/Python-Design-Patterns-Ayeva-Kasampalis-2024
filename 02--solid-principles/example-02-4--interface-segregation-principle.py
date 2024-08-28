"""
*Interface segregation principle* (ISP) =
A class should not be forced to implement interfaces it does not use.
In the context of Python, this implies that a class shouldn't be forced
to inherit and implement methods that are irrelevant to its purpose.
"""


# - Anti-example with no ISP
class AllInOnePrinter:
    def print_document(self):
        print("Printing")

    def scan_document(self):
        print("Scanning")

    def fax_document(self):
        print("Faxing")

# How to implement SimplePrinter?


# - Example with ISP
from typing import Protocol


class Printer(Protocol):
    def print_document(self):
        ...


class Scanner(Protocol):
    def scan_document(self):
        ...


class Fax(Protocol):
    def fax_document(self):
        ...


class AllInOnePrinter:
    """ Implements the three interfaces. """
    def print_document(self):
        print("Printing")

    def scan_document(self):
        print("Scanning")

    def fax_document(self):
        print("Faxing")


class SimplePrinter:
    def print_document(self):
        print("Simply Printing")


def do_printing(printer: Printer):
    printer.print_document()


if __name__ == "__main__":
    all_in_one = AllInOnePrinter()
    all_in_one.scan_document()
    # Scanning
    all_in_one.fax_document()
    # Faxing
    do_printing(all_in_one)
    # Printing

    simple_printer = SimplePrinter()
    do_printing(simple_printer)
    # Simply Printing
