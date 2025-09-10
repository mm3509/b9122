# Speed

If Autograder flags your code for slowness, please read this document: it provides some examples to make your code run faster.

## Use native operations

As seen in lecture 2, some methods are faster than others, and I list them here:

- instead of `.insert(0, ...)`, change your logic to use `.append()`

## Avoid loops

Loops can be slow in Python. Python is optimized so that built-in functions and operations run a lot faster than loops.

For example, consider this example ([source](https://medium.com/@tententgc/vectorization-vs-loops-the-secret-to-massive-python-performance-gains-af8a4ac17234)), which computes the sum of integers up to 1.5 million:

``` python
import time 


N = int(1.5e6)


start = time.time()

total = 0
for item in range(N):
    total += item

end = time.time()

print(round(end - start, 3), "seconds")
# 0.208 seconds
```

If instead we use the built-in function `sum()`, the code becomes 4-5 times faster:

```
import time


N = int(1.5e6)


start = time.time()
total = sum(range(N))
end = time.time()

print(round(end - start, 3), "seconds")
# 0.046 seconds
```

NumPy is optimized further because it compiles down to C, and code doing the same logic is 26 times faster than a loop:

``` python
import time
import numpy as np


N = int(1.5e6)


start = time.time()
total = np.sum(np.arange(N))
end = time.time()

print(round(end - start, 3), "seconds")
# 0.008 seconds
```

## Don't check arguments inside a recursive function

If using recursion, don't check arguments and defensive programming in the recursive function. Instead, write a wrapper function whose only purpose is to check arguments once, and then call a recursive function that does not check arguments and runs fast.

Consider this example of factorial, where I check for the argument each time:

``` python
import time


N = int(9e2)


def factorial(n):

    if not isinstance(n, int):
        raise ValueError("Not an integer!")

    if n < 0:
        raise ValueError("Not a positive integer!")

    if n == 0:
        return 1

    return n * factorial(n - 1)


start = time.time()
factorial(N)
end = time.time()
milliseconds = 1000 * (end - start)
print(round(milliseconds, 3), "ms")
# 0.454 ms
```

If `n` is an integer, `n - 1` will be too. And if it does not hit the terminal case of `n == 0`, then `n - 1` is also non-negative. So we can check for corner cases only once, at the start of the calculation.

I can define an inner recursive function, which only I intend to call and with correct arguments (we'll see how in Object-Oriented Programming) and define an outer imperative function to check the arguments and call this recursive function:


``` python
import time


N = int(9e2)


def factorial_recursive(n):

    if n == 0:
        return 1

    return n * factorial_recursive(n - 1)


def factorial(n):

    if not isinstance(n, int):
        raise ValueError("Not an integer!")

    if n < 0:
        raise ValueError("Not a positive integer!")

    return factorial_recursive(n)


start = time.time()
factorial(N)
end = time.time()
milliseconds = 1000 * (end - start)
print(round(milliseconds, 3), "ms")
# 0.428 ms
```

The code is 6% faster with this improvement.

The improvement is more dramatic in a recursion with a list of size `N` if we check for the type of each list element inside the recursion. In that case, we're checking the last element `N` times, the second to last element `N - 1` times, and so on. Overall, we would be doing `N * (N - 1) / 2` checks, which can be a lot more than the required number of only `N` checks.
