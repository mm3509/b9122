# Grading / guidance on style

Autograder will give you feedback on your style and flag any issues.

For example, this code:

``` python
z = x+y
```
 
will show this error `E225: missing whitespace around operator`. Autograder will also show you a link where you can learn more about it, or you can visit this generic link (replacing `E225` with your error code).

https://www.flake8rules.com/rules/E225.html

## Running style checks locally

You can run style checks locally (on your computer, without waiting
for a GradeScope report) by installing `flake8` from a shell:

```bash
pip install flake8
```

and then checking the style on this file with either of these commands:

``` bash
# After "sourcing" my code, or "hooking" your shell to my code, you can run
# this:
b9-style path/to/file

# Alternatively, run this:
flake8 path/to/file --ignore=E501,W504,E128,E127,E303,E251,W291,W391,E302,E305,E241,E261,E261,F841,E124,W292,W293,W503,W504
```

When you run this, or when it runs on Gradescope, you will get an error such as:

```
compound_interest.py:171:12: F821 undefined name 'days_in_monthh'
```

This indicates that the source of the error:

- is in the file `compound_interest.py`

- on line 171

- on the 12th character of the line

- the machine-readable error has code F821 (and you can read about it at    https://www.flake8rules.com/rules/F821.html )

- the human-readable error means that one variable name is not defined (in this case, it's a typo and has an extra `h` at the end)

## function length

For assignment 2 and the midterm, we expect functions to be under 40 lines (this feature is not yet on Autograder).

A statement that runs over multiple lines counts as one line, for example this long function call:

```python
return some_recursive_function(balance,
                               base_rate,
                               bonus_rate,
                               transactions,
                               recursive_counter + 1)
```

The treatment of edge cases that raise errors do not count as line length.

The treatment of edge cases that do raise errors are part of the function's logic and count towards function length.

## ternary operators

We encourage you to use ternary operators to make functions shorter. These operators condense the code and are still readable. The following three examples are equivalent, but they get shorter.

Here is a typical conditional:

```python
if a <= 0:
    b = "positive_or_zero"
else:
    b = "negative"
```

Here is the same result, but we initialize a variable at a default value:

```python
b = "positive_or_zero"
if a < 0:
    b = "negative"
```

And her is the same result with a "ternary" operator ("ternary" because it uses three arguments: `"positive_or_zero"`, the boolean `a >= 0`, and `"negative"`):

```python
b = "positive_or_zero" if a >= 0 else "negative"
```

## 80-character limit

You have to keep your lines of code under 80 characters (79 or less).

Here is an example of a long line, over 80 characters:

``` python
if np.any(a <= 0):
    raise ValueError("All elements in the input array must be strictly positive.")
```

which you can refactor into two shorter lines under 80 characters:

``` python
if np.any(a <= 0):
    message = "All elements in the input array must be strictly positive."
    raise ValueError(message)
```

Here is another example of a long line in doc-tests, over 80 characters:

``` python
    >>> compute_variance_of_log_growth(np.array([[33], [21], [4], [81]]).astype(float))
```

which you can refactor into two shorter lines under 80 characters:

``` python
>>> a = np.array([[33], [21], [4], [81]]).astype(float)
>>> compute_variance_of_log_growth(a)
```
