import time
import random


def find_triplets(alist):
    """
    >>> find_triplets([0, 1, 1])
    []
    >>> find_triplets([0, 0, 0])
    [[0, 0, 0]]
    >>> find_triplets([-1, 0, 1, 2, -1, -4])
    [[-1, -1, 2], [-1, 0, 1]]
    >>> find_triplets(123)
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> find_triplets([1, 2, "3"])
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    # TODO: add defensive programming.

    # TODO: implement the function.

    return all_triplets


def find_triplets_fast(alist):
    """
    >>> find_triplets_fast([0, 1, 1])
    []
    >>> find_triplets_fast([0, 0, 0])
    [[0, 0, 0]]
    >>> find_triplets_fast([-1, 0, 1, 2, -1, -4])
    [[-1, -1, 2], [-1, 0, 1]]
    >>> find_triplets_fast(123)
    Traceback (most recent call last):
    ...
    AssertionError...
    >>> find_triplets_fast([1, 2, "3"])
    Traceback (most recent call last):
    ...
    AssertionError...
    """

    # TODO: add defensive programming.

    # TODO: implement the function.

    return all_triplets


# Students: this is how you can run code when the file is run directly as a
# script, but not when it's imported as a module. It uses a "dunder" variable,
# `__name__`, which equals `"__main__"` when called directly, and the file's
# name when imported. This way, when Autograder imports your file, it doesn't
# print any output.
if __name__ == "__main__":

    # Students: this code helps you optimize your fast version. It generates a
    # long input and measures how long your slow and fast version take.

    random.seed(42)

    n = int(5e2)
    alist = list([random.randrange(-n, n) for _ in range(n)])

    start = time.time()
    find_triplets(alist)
    print("Slow version:", time.time() - start)

    start = time.time()
    find_triplets_fast(alist)
    print("Fast version:", time.time() - start)
