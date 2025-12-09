import time
import random


def check_argument(alist):
    assert isinstance(alist, list)
    assert all([isinstance(a, int) for a in alist])


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

    check_argument(alist)

    # Sorting here ensures that the triplets are in sorted order, so we don't
    # have to sort them before returning.
    alist = sorted(alist)

    all_triplets = []

    n = len(alist)
    for i in range(n):
        for j in range(i + 1, n):
            current_sum = alist[i] + alist[j]
            for k in range(j + 1, n):
                if alist[k] != - current_sum:
                    continue
                triplet = sorted([alist[i], alist[j], alist[k]])
                if triplet in all_triplets:
                    continue
                all_triplets.append(triplet)

    return all_triplets


def generate_pair_sums(alist):

    # Student: this function is refactored to help the other function stay
    # near 20 lines.

    alist = sorted(alist)
    n = len(alist)
    pair_sums = {}

    for second_index in range(n):
        for third_index in range(second_index + 1, n):
            pair_sum = alist[second_index] + alist[third_index]
            doublet = [(second_index, third_index)]
            pair_sums[pair_sum] = pair_sums.get(pair_sum, []) + doublet

    return pair_sums


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

    check_argument(alist)

    n = len(alist)
    alist = sorted(alist)
    pair_sums = generate_pair_sums(alist)

    all_triplets = []

    # Students: to avoid duplicates, we can either keep track of the last
    # element we saw, and skip it if it's equal, or remove the negative of the
    # element from the dictionary, since any triplet from it will be a
    # duplicate. In this solution, I do both, but only one is necessary.

    previous_first_element = None

    for first_index in range(n):
        first_element = alist[first_index]

        if first_element == previous_first_element:
            # continue
            pass

        previous_first_element = first_element

        pairs = pair_sums.get(-first_element)

        if None is pairs:
            continue

        for pair in pairs:
            # Emulate the nested loop of the slow version, and skip if the
            # first_index is not the smallest of the triplet.
            if min(pair) <= first_index:
                continue

            triplet = sorted([first_element, alist[pair[0]], alist[pair[1]]])

            if all_triplets and triplet == all_triplets[-1]:
                continue
            all_triplets.append(triplet)

            # Remove the pair, because any other time that the above line hits
            # is a duplicate triplet. We could also delete a key-value pair
            # like this:

            # del pair_sums[-first_element]

            pair_sums[-first_element] = None

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
