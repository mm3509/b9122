import random


def approximate_pi(n):

    assert isinstance(n, int) and n > 0

    random.seed(0)

    inside_unit_circle = 0

    for _ in range(n):
        x = random.random()
        y = random.random()
        radius_squared = x ** 2 + y ** 2
        
        # Count this with the conversion of booleans to integers:

        # inside_unit_circle += (radius_squared < 1)

        # Alternatively, use a conditional:
        if radius_squared < 1:
            inside_unit_circle += 1

    p_hat = inside_unit_circle / n

    return p_hat * 4


for exponent in range(10):
    n = int(10 ** exponent)
    print(f"At n = 10^{exponent}, pi = {approximate_pi(n)}")
