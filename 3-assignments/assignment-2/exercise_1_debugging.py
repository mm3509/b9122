import random
import string


def extend_list_with_variations(a_list):
    """
    >>> a_list = ["one", "two", "three"]
    >>> extend_list_with_variations(a_list)
    ['one', 'two', 'three', 'ome', 'tyo', 'thnee']
    >>> extend_list_with_variations(123)
    Traceback (most recent call last):
    ...
    AssertionError
    """

    # Students: no need to add defensive programming, it's already
    # done here. Two corner cases use list comprehensions, which the
    # afternoon section will see in lecture 6.
    assert isinstance(a_list, list)
    assert all([isinstance(word, str) for word in a_list])
    assert all([len(word) > 0 for word in a_list])

    # Students: this line sets the seed and ensures reproducibility,
    # so the doc-tests can pass without randomness.
    random.seed(a=0)

    for word in a_list:
        replacing_index = len(word) // 2
        replacing_letter = random.choice(string.ascii_lowercase)
        new_word = (word[:replacing_index]
                    + replacing_letter
                    + word[replacing_index + 1:])
        a_list.append(new_word)

    return a_list
