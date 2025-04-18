"""
Iterator

The *Iterator* pattern is a design pattern, in which an *iterator* is used to traverse a container and
access the container's elements.
The iterator pattern decouples algorithms from containers.
In some cases, algorithms are necessarily container-specific and thus cannot be decoupled.
Iterator in Python is simply an object that can be iterated upon
that is, an object that will return data, one element at a time.
"""

# Example: Implement the *iterator* protocol

# Define the `__iter__` and `__next__` methods
class FootballTeamIterator:
    def __init__(self, members):
        self.members = members
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.members):
            value = self.members[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration()


# Define the `__iter__` method
class FootballTeam:
    def __init__(self, members):
        self.members = members

    def __iter__(self):
        return FootballTeamIterator(self.members)


# Use the build-in functions `iter` and `next`
def main():
    members = [f"player{str(x)}" for x in range(1, 23)]
    members = members + ["coach1", "coach2", "coach3"]
    team = FootballTeam(members)
    # Create the iterator
    team_iter = iter(team)

    try:
        while True:
            print("in `while`:", next(team_iter))
    except StopIteration:
        print("(End)")

    for member in team:
        print("in `for`:", member)


if __name__ == "__main__":
    main()
    # in `while`: player1
    # ...
    # in `while`: player22
    # in `while`: coach1
    # in `while`: coach2
    # in `while`: coach3
    # (End)
    # in `for`: player1
    # ...
    # in `for`: player22
    # in `for`: coach1
    # in `for`: coach2
    # in `for`: coach3
