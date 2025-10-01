import math

# Students: uncomment if you want to use NumPy.
# import numpy as np 

from solution_2_annualize import DAYS_IN_YEAR


def diarize_return(interest_rate):
    """
    >>> round(diarize_return(0.28387), 3)
    0.001
    >>> diarize_return('0.28')
    Traceback (most recent call last):
    ...
    AssertionError
    """

    assert isinstance(interest_rate, (int, float))

    # Students: here is the NumPy version:
    # return np.exp(np.log(1 + interest_rate) / DAYS_IN_YEAR) - 1

    # Students: equivalent solution, without the math module
    # return (1 interest_rate) ** (1 / DAYS_IN_YEAR) - 1

    return math.exp(math.log(1 + interest_rate) / DAYS_IN_YEAR) - 1



