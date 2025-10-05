# Assignment 2

The maximum comment share for this assignment is 40%: for every 10 lines that you add in the code, at most 4 should be comments.

To practice defensive programming, this assignment gives one doc-test for corner cases. You will have to anticipate what other corner cases could occur for the first 10 days of the assignment. In the last 2 days, Autograder will reveal the corner cases, one at a time.

For MSAFA: the last 3 questions cover recursion and are optional. They increase your grade up to the maximum of 140 points, but do not carry over to other assignments.

## 1: Debugging (20 points for MSFE, 40 points for MSAFA)

To generate a list of strings as test inputs for your exercises on Autograder, I may need to duplicate a list of strings with some changes (for example, from a list of IBANs, I modify them slightly so the `is_same_iban()` from assignment 1 will fail).

This exercise has a bug and never finishes, i.e. it has an infinite loop. Find the bug, fix it, and add a comment explaining the bug. (You don't need to add defensive programming. For this question only, your maximum share of comments is 80%, i.e. if you change one line of code, you can add 4 lines of coments.)

## 2: Polynomials (20 points for MSFE, 50 points for MSAFA)

Complete the function to compute the value of a polynomial, where the first argument is `x`, and the second argument is a list with the polynomial's weights:

```
f(x, A) = A[0] + A[1] * x + A[2] * x^2 ... + A[n] * x^n
```

Implement strict defensive programming, assuming that anyone may call your function with arguments that are invalid for a mathematical polynomial calculation (but without worrying about physical limits, like the maximum number for a float).

Implement a first simple version of the function to pass the doc-tests. Then implement the second version, with suffix `_fast`, with [Horner's method](https://en.wikipedia.org/wiki/Horner%27s_algorithm) to pass speed (linear complexity instead of quadratic complexity).

In either function, you may not use built-in fast functions like `sum()` or `np.sum()`.

## 3: Moving Average (20 points for MSFE, 50 points for MSAFA)

The moving average of an array `A` with window size `k` is `None` for the first `k - 1` elements, and otherwise:

```
moving_average[i] = (A[i - k + 1] + A[i - k + 2] + ... + A[i]) / n
```

Implement strict defensive programming, assuming that anyone may call your function with arguments that are invalid for a mathematical calculation of the moving average (but without worrying about physical limits, like the maximum number for a float).

Complete the first function to implement this moving average. Optimize the second function so it gives the same results as the first, but is faster and passes the speed test.

In either function, you may not use built-in fast functions like `sum()` or `statistics.mean()`.

## 4: Recursion (20 points for MSFE, 5 optional points for MSAFA)

This exercise is an example of a problem that can only be solved through recursion.

A list in Python can contain anything, including other lists. Sometimes, you get unstructured data from the internet or from a company, you want to "flatten" a list so it does not contain other lists inside it (i.e., avoiding "nested lists").

First, experiment with the list method `.extend()`: if `a` and `b` are lists, `a.extend(b)` produces the same results as `a += b`, but is more efficient (similar to how `a.append(1)` is more efficient than `a += [1]`).

Add defensive programming. In this question, the list argument can contain anything, like in Python.

Implement the function to flatten a list, while maintaining the order in which the elements appear.

## 5: Excel column letters to number (30 points for MSFE, 5 optional points for MSAFA)

Note: this exercise is from the waiver exam.

This exercise converts Excel column letters into numbers.

Add defensive programming, assuming that:

- anyone may call your function with arguments that are not valid strings for an Excel column;

- Excel has no limitation on the number of columns (we don't consider physical limits in this course).

Complete the function to pass the doc-tests, either in recursive or in imperative programming. You may not use external libraries like `openpyxl`.

## 6: number to Excel column letters (30 points for MSFE, 5 optional points for MSAFA)

Note: this exercise is from the waiver exam.

This exercise is the reverse of the previous exercise and converts numbers into Excel column letters.

Add defensive programming, assuming that:

- anyone may call your function with arguments that are not valid for an Excel column number;

- Excel has no limitation on the number of columns (we don't consider physical limits in this course).

Complete the function to pass the doc-tests, either in recursive or in imperative programming. You may not use external libraries like `openpyxl`.
