# Students: you may not use the rand module other than what is already
# written.
import random

def fair_coin():
    return random.randrange(2)


def simulate(p):

    # The current function always returns True, which is 100% chance
    # of winning.  If you return False, it's 0% chance of winning. You
    # have to return True with probability p, and False with
    # probability (1-p). For example, if p=0.2 and we run
    # simulate(0.2) 100 times, on 20 times it returns True and the
    # other 80 times it returns False. But this function returns only
    # one boolean at a time, so that boolean (True or False) has to be
    # random, thanks to calling the function fair_coin().

    # TODO: implement this function, without defensive programming

    return


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
