# DRY / Don't Repeat Yourself

This document explains our human judgment on what constitutes "DRY" (Don't Repeat Yourself) code as opposed to "WET" (We Enjoy Typing).

As a rule-of-thumb, if you ever find yourself copy-pasting code, consider "refactoring" that piece of code you were about to copy into:

- a loop

- a variable that you use multiple times

- a function that you can call

- a module that you can import

When code is DRY, each variable, function or module is defined in one place, and one place only. programmers called this "Single Source of Truth".

## example with a loop

In lecture 2, we saw this code:

``` python
print("This is a list of the largest public companies")
print("Nvidia")
print("Microsoft")
print("Apple")
print("Alphabet (Google))"
print("Amazon")
```

If we want to print `Name: ` before each company, we would have to add it in 5 places. Making a change in multiple locations is a sign of WETness.

Instead, consider the "refactored" code with a loop:

``` python
print("This is a list of the largest public companies")
companies = ["Nvidia", "Microsoft", "Apple", "Google", "Amazon"]
for company in companies:
    print(company)
```

We can now add `Name: ` with a single change:

``` python
print("This is a list of the largest public companies")
companies = ["Nvidia", "Microsoft", "Apple", "Google", "Amazon"]
for company in companies:
    print("Name:", company)
```

## example from math

The concept of "refactoring" in programming is similar to "factoring" in math.

This expression is called "distributed":

```python
a + a + a + a + a
```

and has the same value as this expression, which is "factored":

```python
5 * a
```

but the latter is shorter, simpler, easier to read, and less likely to have bugs.
