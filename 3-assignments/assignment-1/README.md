# Assignment 1

Exercises 1 and 7 require the `yfinance` package. To install it, run this in a shell (Terminal.app or git bash):

``` bash
python -m pip install yfinance
```

Several exercises use ASCII, the American Standard Code for Information Interchange. ASCII letters are uppercase or lowercase letters from A to Z. ASCII digits are 0-9. You can access them with:

``` python
import string

print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.digits)
```

In defensive programming, for technical reasons, you should raise a `ValueError` (and not a TypeError, unlike what I mentioned in lecture 2).

Some exercises are optional for MSAFA and MSM students: you can answer these exercises to get points up to a maximum of 140, but you cannot "save and transfer" these points to assignment 2.

## 1: converting currencies (20 points for MSFE, 35 points for MSAFA + MSM)

This exercise uses code already written to convert a currency. The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) standard defines a currency with three ASCII letters. You can assume that, if the user passes three ASCII letters, that is a valid currency code; if not, you can let the call to Yahoo throw an error.

The exercise is missing corner cases. Add defensive programming for
all cases you can think of. (Autograder will only give your score on
defensive programming and corner cases after the deadline.)

## 2: annualize a return (20 points for MSFE, 35 points for MSAFA + MSM)

We will sometimes need to convert a return (like an interest rate or a stock return) from a time period to another. This exercise converts a daily return to a yearly return, assuming that a year has 250 days (the approximate number of trading days in a year).

Add code to the function to pass the doc-tests. Add defensive programming. Use the operator `**` for exponentiation.

## 3: diarize a return (20 points for MSFE, 35 points for MSAFA + MSM)

This exercise is the reverse of the previous: it converts an interest rate from annual to daily.

Using the functions `math.log()` and `math.exp()` (or, alternatively, use the NumPy versions: `np.log()` and `np.exp()`), add code to pass the doc-test. Also add defensive programming.

## 4: remove duplicate and contiguous lines from a file (20 points for MSFE, 35 points for MSAFA + MSM)

Sometimes, your code writes a result into a file. If you run it twice, it will write the result twice to the file. This exercise removes those duplicate lines if they are immediately next to each other.

The first function in this exercise removes duplicate elements from a list of strings. Add defensive programming. Add code to pass the doc-test.

The second function is for reference, for you, in case you later want to use the first function on a filepath. You needn't do anything.

## 5: string to integer cents (20 points for MSFE, bonus question for MSAFA + MSM for 5 points)

Floats have the problem of losing precision; for example `.1 * 3 == .3` returns `False` because of numerical errors in the representation of floating point numbers. That is why e-commerce companies like Stripe first convert any currency into an integer number of **cents**, do all the calculations in integers (such as sales tax), then convert back to dollars and cents to show the user.

This exercise converts a string into an integer number of cents.

Add defensive programming. You can use the string method `.count()`: `a.count(b)` returns the number of occurrences of string `b` in string `a`.

Add code to pass the doc-tests.

## 6: check IBAN (20 points for MSFE, bonus question for MSAFA + MSM for 5 points)

Some homebanking sites do not let you copy-paste an IBAN when making a transfer (some say that it makes transfers harder for thieves, but I am not convinced). Instead, you have to write the IBAN by hand. Although IBANs have a built-in system for checking correctness (the last two digits confirm whether the IBAN is valid, and so prevent typos), I prefer to double-check that the IBAN in the confirmation page of the transfer (where I can copy-paste) is the same as in my files, which is why I wrote this function.

The first function cleans the IBAN, ignoring spaces, periods, and letter case (including at the beginning and the ending, because of copy-pasting). It throws an error if it is invalid. An IBAN is valid if and only if:
- it starts with two ASCII letters (don't verify if the country exists)
- it has any positive number of digits and ASCII letters (and it can have spaces and periods too)
- it ends with 2 digits

Add defensive programming and code to the first function. Use the string method `.replace()`, i.e. `a.replace(b, c)` replaces all occurrences of `b` with `c` in string `a` and returns a new string.

The second function returns True if the two IBANs are valid and are the same, after being cleaned by the above function. Add code to pass the doc-tests. You needn't add defensive programming to this second function, because the call to `clean_iban()` covers corner cases.

## 7: debugging (20 points for MSFE, bonus question for MSAFA + MSM for 5 points)

This file calls the function in exercise 1 to print currency conversions from the shell. For example, we want to write:

``` bash
python exercise_7_debug.py 1000 USD EUR
```

If you want to use this interactively from a shell, e.g. you want compute your bank's commission on an international transfer, you would want to see a human-readable result:

```
USD 1,000.00 = EUR 850.10
```

Alternatively, if you want to use this function programmatically, then you would not want to print the converted value, only to return it (for further handling by another Python function).

Read the code to learn how Python accesses shell arguments: `sys.argv[0]` is the name of the file, `sys.argv[1]` is the first argument (1000 in the case above), etc.

The code has a bug. Use the methods from class to find the bug and fix it. Add a comment in the code to explain the bug.

You needn't add any defensive programming, you only need to solve the bug.
