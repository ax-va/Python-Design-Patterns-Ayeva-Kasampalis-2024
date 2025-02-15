"""
*Single Responsibility Principle* (SRP) =
Each class should have one job or responsibility,
and that job should be encapsulated within that class.
"""


# - Anti-example with no SRP
class Report:
    """
    Anti-example:
    The Report class has two responsibilities:
    1. generating a report;
    2. saving the report's content to a file.
    """
    def __init__(self, content):
        self.content = content

    def generate(self):
        print(f"Report generated: {self.content}")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(self.content)


# - Example with SRP:
# Separate responsibilities in two different classes,
# each of which is with only one responsibility.
class Report:
    """ Is responsible for generating the report's content. """
    def __init__(self, content):
        self.content = content

    def generate(self):
        print(f"Report generated: {self.content}")


class ReportSaver:
    """ Is responsible saving the report's content to a file. """
    def __init__(self, report: Report):
        self.report: Report = report

    def save_to_file(self, filename: str):
        with open(filename, 'w') as file:
            file.write(self.report.content)


if __name__ == "__main__":
    report_content = "This is the content."
    report = Report(report_content)
    report.generate()
    # Report generated: This is the content.

    report_saver = ReportSaver(report)
    report_saver.save_to_file("report.txt")
