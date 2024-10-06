# Grading / guidance on style

We will build gradually over the term to a good coding style. I will add style rules gradually on GradeScope and you will get immediate feedback.

## Google Python Style Guide

For general guidance and examples of good style, please check the [Google Python Style
Guide here](https://google.github.io/styleguide/pyguide.html).

## Specific errors from GradeScope

For specific guidance on each error, for example `E225: missing whitespace around operator`, check a link such as this (replacing the end code, before `.html`, with your error code):

https://www.flake8rules.com/rules/W293.html

## Running style checks locally

You can run style checks locally (on your computer, without waiting
for a GradeScope report) by installing `flake8` from a shell:

```bash
pip install flake8
```

and then checking the style on this file (ignoring the same errors as GradeScope for assignment 2) with:

flake8 'FILEPATH' --ignore=E501,W504,E128,E127,E303,E251,W291,F401,W391,E302,E305,E241,E261,E231,E261,F841,E124,W292,W293,W503,W504

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