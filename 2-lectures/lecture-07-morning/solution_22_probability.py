# Students: you may not use the rand module other than what is already
# written.
import random

def fair_coin():
    return random.randrange(2)


def simulate(p):
    """
    >>> simulate("ab")
    Traceback (most recent call last):
    ...
    AssertionError
    >>> simulate(1.1)
    Traceback (most recent call last):
    ...
    AssertionError
    """

    assert isinstance(p, (int, float)) and 0 <= p and p <= 1

    while True:
        p *= 2
        p_i = int(p)
        s_i = fair_coin()

        if s_i < p_i:
            return True
        if p_i < s_i:
            return False

        p -= p_i


def test_simulator(p, N=int(1e5)):
    """
    >>> success_rate = test_simulator(0.7)
    >>> round(success_rate, 2)
    0.7
    >>> success_rate = test_simulator(0.2)
    >>> round(success_rate, 2)
    0.2
    """
    # This next line ensures reproducibility for the function to pass
    # the doc-tests.
    random.seed(0)
    
    success = 0
    for _ in range(N):
        success += int(simulate(p))

    return success / N
