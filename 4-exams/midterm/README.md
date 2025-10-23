---
title: 'Midterm exam (B9122, Computing for Business Research)'
author: 'Miguel Morin, (c) 2025'
geometry: margin=2cm
numbersections: false
header-includes:
- \pagenumbering{gobble}
- \setlength{\parskip}{\baselineskip}
- \usepackage{hyperref}
- \usepackage{xcolor}
- \newcommand{\link}[1]{{\color{blue}\underline{\href{#1}{#1}}}}
---

# Midterm exam

AFA + Marketing: the exercises are roughly in order of increasing difficulty. I do not expect you to complete all of them. I will adjust the difficulty of the exam afterwards because I apply a curve by section before converting to a letter grade.

In all exercises but the debugging exercises, you should implement defensive programming and implement the function to pass the doc-tests.

Each exercise has a use case that is just for context, for you to understand the problem and find corner cases. You do not need to do anything more about it.

You have unlimited uploads on Autograder for the duration of the exam.

On corner cases:

- do not worry about physical limits, such as a float or an integer being infinity; don't worry about a number being `NaN` either;

- Autograder does not check defensive programming in the first half of the exam; in the second half it will reveal the corner cases you did not cover, one per submission and per exercise, with an artificial delay of 1-2 minutes for each corner case covered.

On comments:

- Debugging questions have a maximum of 90% comment share; other questions have a maximum of 40%.

- If you copy code from the internet, you have to provide attribution in a comment (but Autograder ignores these comments when computing your comment share). You can add `# noqa: E501` at the end of that line to avoid style errors.

The template files are on Canvas as a ZIP file. You can double-click to extract the files (on macOS) or to view them (on Windows, which you can then copy). Please ask us for help if you need.

## 1: stock profitability (5 points for MSFE, 18 points for MSAFA)

This function takes two arguments, a buying and selling price, and returns the percentage growth in the price.

The prices have to be strictly positive.

Use case: you want to monitor when a stock drops or rises by more than 10%, so you can decide whether to buy or sell.

## 2: debugging with ZIP codes (MSAFA only, 20 points)

This function returns whether a string is a valid ZIP code in the US (where ZIP codes are digits) or in the UK (where ZIP codes can contain letters). It has a bug and does not pass the doc-tests. Find it, add a comment to explain it, and fix it.

## 3: UNI to program (9 points for MSFE, 22 points for MSAFA)

This function takes two arguments:

- a string with an email address

- a dictionary, where the keys are UNIs and the values are the MS program where that UNI is registered.

The function returns a string with a program (which is the value of the key-value pair in the dictionary for the person represented by the email), or returns `"both"` (if the email is not represented in the dictionary). (Why use a dictionary instead of two lists? Because with a dictionary, we are sure that keys are unique, so a UNI can only be in one program, and it saves us from several corner cases.)

Use case: Autograder allocates you directly into the right section, without asking you which program you are in thanks to a dictionary. When the TAs test the Autograder before the release date, they are not in a program, but Autograder does not throw an error and grades all the questions (not just the questions for one program or the other).

For simplicity, a string is a valid email if and only if all of these conditions are met:

- it contains only ASCII letters, digits, periods (`.`), underscores (`_`) and at-symbol (`@`)

- it contains one and only one character `@`

- the username (before the `@` character) has at least 2 letters and starts with a letter (i.e., the first character has to be a letter, and there should be another letter in the username)

(Note: these rules mimic those for most Columbia and Gmail addresses.)

A dictionary is valid if and only if it's non-empty. (When testing your function, Autograder uses your actual UNIs and programs, with the last 2 digits removed for privacy.)

AFA students: to get the string before the `@`, read about the string method `.split()`, which splits a string into a list. You can also use the variables `string.ascii_letters` and `string.digits` from the `string` package.

## 4: range to integer list (13 points for MSFE, 24 points for MSAFA)

This function takes as argument a string with a human-readable range of pages, like `"1-5,7"`, and returns a list of integers with the pages in the range.

Use case: You program a printer to print a document by specifying page ranges (like `1-5,7`, without writing `1,2,3,4,5,7`) so that the printer will print pages 1 to 7 and skip page 6.

For simplicity of corner cases, a range is valid if and only if it has only digits, commas (`,`) and dashes (`-`). If so, then you can assume that the range is valid. (That is, I do not expect you to cover corner cases like `-2,`, nor `0-10`.)

Note: you can use the string method `.split()` as in the previous exercise; and the string method `a.count(b)`, which returns the number of ocurrences of string `b` in string `a`.

## 5: integer list to range (17 points for MSFE, 26 points for MSAFA)

This function does the inverse of the previous function. It takes as argument a list of unique (i.e., not repeated) integers and returns a string with that list in a human-readable format with ranges.

Use case: You have prepared 20 training sessions for users (for example, the next recruits at your employer) and are reporting on their use of your sessions. You want to convey the use by each user without losing information. For example, a user who attended all sessions will have a string `'1-20'`, whereas a user who missed session 5 will have `'1-4,6-20'`. For simplicity, each session is a integer.

## 6: merge solution slides (20 points for MSFE, 30 points for MSAFA)

This function takes three arguments:

- the number of pages of the lecture slides before lecture;

- the number of pages of the lecture slides after lecture, with additional slides for solutions;

- a list (possibly empty) of unique (i.e. not repeated) integers, representing pages from the solution slides, to be added to the original slides.

The function returns a list with integers. The elements of the return list are the final position of the merged slides. Negative integers point to pages from the original slides; positive integers point to pages in the solution slides.

Use case: you download the lecture slides before lecture and annotate them. After lecture or before an exam, you don't want to review two PDFs. Instead, you want to merge the additional pages from the solutions PDF (and those pages only) to the PDF that already has your annotations. In the end, it's almost as if you had been annotating the PDF with solutions during lecture. (In software, this is called "back-porting", moving data into a past version.)

For example: the original slides have 5 pages; the solution slides have 6 pages, and page 5 from the solution slides is an additional page, which should come between pages 4 and 5 from the original PDF. Your function should return: `[-1, -2, -3, -4, 5, -5]`.

## 7: debugging (MSFE only, 21 points)

In class we saw that some integers in Python (between -5 and 256) are unique (i.e., Python keeps a unique copy of the integer) so we could compare them with `is` (by reference, on the memory address). Other integers (lower than -6 or higher than 257) are not unique (i.e., Python can keep multiple copies of them), so we have to compare them with `==` (by value).

Now imagine that you did not know those two bounds (-5 and 256), or that those bounds had changed in a new version of Python, and that you could not find them in the documentation. How could you find those bounds? This exercise is one way to find that upper bound with code.

This function takes one argument, an integer. It returns the first integer after the argument that does not have a unique memory address (i.e., where we have to compare with `==`). It has a bug and does not pass the doc-tests. Find and understand the bug, fix it, and add comments to explain the bug.

## 8: formatting money (25 points for MSFE, optional 5 points for MSAFA)

This function takes a number representing a money amount, either positive or negative (profit or loss), but smaller than 1000 in absolute value. It returns a string of length 7 where the period (if any) is always at the same position (position 5, or third to last) for easy reading. For Autograder testing, the input will always have at most two digits after the decimal point (i.e., an integer number of cents divided by 100).

As it is common in real life programming and in interviews, the code to solve this problem can range from very simple to very messy depending on the approach you take. Before starting to write code, we suggest that you spend a few minutes thinking of different ways to solve the problem and go with the one that would lead to the simplest, most easily debuggable solution.

Below are several examples (taken from the doc-tests). (The input may be `910.1` because it can come from some other calculation, such as `1910 - 999.9`.)

```
'  20   '  # if the input is 20
' -20.01'  # if the input is -20.01
' 910.16'  # if the input is 910.16
' 910.10'  # if the input is 910.1
'-100   '  # if the input is -100
'   0   '  # if the input is 0
```

Use case: you analyze the profit or loss from stocks in a portfolio. You want to present these results as strings, in a way that a string with more numbers to the left of the period is always greater in absolute value than a string with fewer numbers.

You may **NOT** use any of these shortcuts: a string method like `.rjust()`, string formatting like `%.2f`, f-strings with `f{amount:.2f}`.

## 9: Autograder (30 points for MSFE, optional 5 points for MSAFA)

Use case: Autograder runs solution files on test inputs, then your exercise files, and compares the two. It should return `True` if they are the same, with a tolerance for numerical error and for calculations done in NumPy.

In assignment 1, several students used NumPy for calculations. NumPy is a module with different numerical precision than core Python, so students got answers that were very similar, such as `48.999999` instead of `49`. Therefore, Autograder should compare numbers with tolerance for numerical error, using the function `np.isclose()` (which is already in the template).

Autograder should also allow NumPy for logic and calculations. For example, if students use the NumPy booleans, `np.True_` and `np.False_` (with type `np.bool_`), Autograder should consider them equivalent to the core Python booleans, `True` and `False` (with type `bool`).

This function takes two arguments, the correct answer and a student's answer. It returns `True` if they have the same values, with tolerance for numerical error and usage of NumPy.

The arguments can be:

- `None`, which is a special object;

- simple objects like integers, floats, strings;

- complex objects like lists or dictionaries (for simplicity, we do not consider tuples).

Complex objects can, in turn contain other objects inside of them (this is called "nesting"). For example, a list can have `None`, a simple object like a float, and a complex object like a dictionary (all in the same list); a dictionary can contain on value that is `None`, another value that is a string, and another value that is a list (which, itself, can contain a dictionary, and so on).

__Example 1__: exercise 3 of assignment 2 returned a list of moving averages, with `None` in case the moving average could not be computed. The solutions might be `[None, 48, 49]`. If you submit `[None, 48, 48.99999]`, that should be correct:

``` python
>>> are_answers_equal([None, 48, 49], [None, 48, 48.99999])
True
```

__Example 2__: a function takes as input a list of ticker codes, and returns a dictionary where each key is one of those ticker codes, and the value is a list with 3 or more elements: a string with the exchange where the ticker is listed, an integer with the latest stock price in cents, a float with profitability over the last month, etc:

``` python
>>> are_answers_equal({"MSFT": ["NYSE", 50000, 0.1]}, {"MSFT": ["NYSE", 50000, 0.099999]})
True
```

For more examples, please see the doc-tests.

There is only one corner case for this exercise (already in the doc-tests): the data type of the answer is not in one of `ALL_DATA_TYPES` (for example: a tuple).

Fun fact: the solution to this exercise is exactly the code running on Autograder right now!
