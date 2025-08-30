import doctest


def get_primes_fast(n):
    """
    >>> get_primes_fast(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    >>> get_primes_fast(11)
    [2, 3, 5, 7, 11]
    """

    # Initialize a list containing whether the integer could be a
    # prime. For simplicity, the index of the list corresponds to the
    # integer, e.g. could_be_prime[n] contains whether n could be a
    # prime number, so the first two elements, for 0 and 1, have to be
    # False.
    could_be_prime = [True for _ in range(n + 1)]
    could_be_prime[0] = False
    could_be_prime[1] = False

    i = 1
    while i ** 2 <= n:
        i += 1
        if not could_be_prime[i]:
            continue

        for multiplier in range(i, n // i + 1):
            multiple = i * multiplier
            could_be_prime[multiple] = False

    return [i for i in range(len(could_be_prime)) if could_be_prime[i]]


if "__main__" == __name__:
    tests_failed, tests_run = doctest.testmod(optionflags=doctest.ELLIPSIS)
    if 0 < tests_run:
        assert 0 == tests_failed, 'Some doc-tests failed, exiting...'
        print('Your doc-tests pass, congratulations!')
    else:
        print('Unable to run doc-tests, please see Miguel!')
