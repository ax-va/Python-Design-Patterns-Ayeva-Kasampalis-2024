"""
Strategy

The *Strategy* pattern promotes using multiple algorithms to solve a problem.
It makes it possible to switch algorithms at runtime transparently that is,
the client code is unaware of the change.
Normally, the strategy should not be picked by the user.

Example:
Use the strategy pattern to determine whether a character sequence has unique characters.
"""
import time
from typing import Generator, Tuple, Sequence, Callable


def pairs(seq: Sequence) -> Generator[Tuple[str, str], None, None]:
    """
    Returns all neighbors pairs of a sequence.

     Args:
         seq: character sequence

    Yields:
        Tuple(<character>, <cyclic next character>)
    """
    n = len(seq)
    for i in range(n):
        yield seq[i], seq[(i + 1) % n]


SLOW = 3  # in seconds
LIMIT = 5  # in characters
WARNING = "too bad, you picked the slow algorithm"


def all_unique_sort(seq: str) -> bool:
    """
    Returns `True` if all characters in the string are unique; otherwise, it returns `False`.
    We make the algorithm slow if the sequence has greater than `LIMIT` characters.
    This is a strategy function.
    """
    if len(seq) > LIMIT:
        print(WARNING)
        time.sleep(SLOW)

    sorted_str = sorted(seq)
    for char1, char2 in pairs(sorted_str):
        if char1 == char2:
            return False

    return True


def all_unique_set(seq: str) -> bool:
    """
    Returns `True` if all characters in the string are unique; otherwise, it returns `False`.
    We make the algorithm slow if the sequence has less than or equal to `LIMIT` characters.
    This is another strategy function.
    """
    if len(seq) <= LIMIT:
        print(WARNING)
        time.sleep(SLOW)

    return True if len(set(seq)) == len(seq) else False


def all_unique(seq: str, strategy: Callable | None) -> bool:
    """
    Executes the input strategy and returns its result to the caller.
    """
    if strategy is None:
        if len(seq) <= LIMIT:
            strategy = all_unique_sort
        else:
            strategy = all_unique_set

    return strategy(seq)


def main():
    word_in_desc = "Insert word (type quit to exit)> "
    strat_in_desc = "Choose strategy: [1] Use a set, [2] Sort and pair > "

    while True:
        word = None
        while not word:
            word = input(word_in_desc)

            if word == "quit":
                print("bye")
                return

            strategy_picked = None
            strategies = {"1": all_unique_set, "2": all_unique_sort}
            while strategy_picked not in strategies.keys():
                # Normally, the strategy that we want to use should not be picked by the user.
                strategy_picked = input(strat_in_desc)

                try:
                    strategy = strategies[strategy_picked]
                    result = all_unique(word, strategy)
                    print(f"all_unique({word}): {result}")
                except KeyError:
                    print(f"Incorrect option: {strategy_picked}")


if __name__ == "__main__":
    main()
    """
    Insert word (type quit to exit)> ballon
    Choose strategy: [1] Use a set, [2] Sort and pair > 1
    all_unique(ballon): False
    Insert word (type quit to exit)> ballon
    Choose strategy: [1] Use a set, [2] Sort and pair > 2
    too bad, you picked the slow algorithm
    all_unique(ballon): False
    Insert word (type quit to exit)> lol
    Choose strategy: [1] Use a set, [2] Sort and pair > 1
    too bad, you picked the slow algorithm
    all_unique(lol): False
    Insert word (type quit to exit)> lol
    Choose strategy: [1] Use a set, [2] Sort and pair > 2
    all_unique(lol): False
    Insert word (type quit to exit)> abcdef
    Choose strategy: [1] Use a set, [2] Sort and pair > 1
    all_unique(abcdef): True
    Insert word (type quit to exit)> abcdef
    Choose strategy: [1] Use a set, [2] Sort and pair > 2
    too bad, you picked the slow algorithm
    all_unique(abcdef): True
    Insert word (type quit to exit)> quit
    bye
    """