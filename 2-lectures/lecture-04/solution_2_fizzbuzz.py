
# Solution with nesting.

for i in range(100):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# Solution without nesting.

def fizzbuzz(i):
    """
    >>> fizzbuzz(1)
    1
    >>> fizzbuzz(3)
    'Fizz'
    >>> fizzbuzz(5)
    'Buzz'
    >>> fizzbuzz(15)
    'FizzBuzz'
    """
    if i % 3 == 0 and i % 5 == 0:
        return "FizzBuzz"

    if i % 3 == 0:
        return "Fizz"

    if i % 5 == 0:
        return "Buzz"

    return i


for i in range(100):
    print(fizzbuzz(i))
