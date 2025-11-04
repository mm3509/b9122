# Assignment 3

30% is the maximum comment share for this assignment; except for question 1, with debugging, for which it is 90%.

Use cases are for you to understand context and anticipate corner cases. You do not need to implement them.

From now on, for readability, your functions should be under 20 lines (ignoring blank lines, comments, and defensive programming). To stay under this limit, you should refactor a long function into smaller helper functions.

## 1: debugging (20 points for MSFE; 40 points for MSAFA)

This function is similar to a problem from the midterm, but now supports amounts up to quintillions of dollars. The input still represents a monetary amount, so it has at most 2 digits in the decimal part.

It has a bug and does not pass the doc-tests.

Read and understand the bug (reading someone else's code is an important part of programming). Your fix to the bug should be minimal, i.e.g changing one or two lines. Do not use f-strings (such as `f"{amount:,})"`) or similar formatting methods.

If needed, learn about new functions and methods in the code.

## 2: string to maximum comment share (20 points for MSFE; 50 points for MSAFA)

Use case: In assignment 2, some of you asked that the maximum comment share for debugging exercises be larger than the default comment share.

This function reads an assignment description in Markdown format and extracts the "comment share" settings. It returns a dictionary with two integer values: 1) in the `default` key: the normal comment share percentage; 2) in the `debug` key: the comment share percentage for debugging exercises, which is higher than the default share.

Here are rules of the input:

1. Only one line in the description may contain the phrase “comment share”.

2. That line can specify: 1) one percentage, which is the default share; or 2) two parts separated by a semicolon (`;`), where one and only one part contains the string `debug`.

3. Percentages must include the `%` sign, and the percentage can appear before or after the string `comment share`.

For example input and outputs, please see the doc-tests.

**Note**: in Python, we represent a newline with `\n`. The backslash is called an "escape character"; together with another character, it represents characters such as newlines (`\n`) or tabs (`\t`). But inside doc-tests, the escape character itself needs to be escaped, so inside a doc-test, a newline is `\\n` (that's because doc-strings are strings that first convert to code, so the double escape character converts to a single escape character, which then applies to the character `n` to produce a newline).

## 3: search algorithm (20 points for MSFE; 50 points for MSAFA)

This function takes a non-empty list of integers and returns a tuple with two elements, the minimum and the maximum, in that list. (See the template file for how to return a tuple.) In this exercise, you cannot use `min()` nor `max()`, nor any other similar functions (`sorted()`, etc).

To find the minimum (or the maximum) in a list of `n` elements, we need to make `n - 1` comparisons  (i.e., the use of the operation `<` or `>`). Write a slow version of the function that implements this simple idea and makes `2 (n - 1)` comparisons.

Nevertheless, when we look for **both** the minimum and the maximum in a list, we can save `(n - 1) / 2` comparisons and make only `3 (n - 1) / 2` comparisons. First, think how you can save that amount of comparisons. Then, implement this in the fast version of the function. Note that the autograder may not be able to distinguish solutions with the right number of comparisons from those with too many comparisons, so please do not rely on Autograder speed to judge whether your fast algorithm is fast enough.

## 4: binary search (25 points for MSFE; optional 5 points for MSAFA)

This function takes a non-empty list of integers. From the beginning of the list until one position, all elements are zero. From that position onwards the elements are non-zero. We want to find the **index** of the first non-zero element but we don't know the length of the list (you may not use `len()`). If there are no non-zero elements in the list, return -1. Write a slow version of the function with a very simple algorithm, to have linear complexity in the number of zero elements.

Now write a fast version of the function using logarithmic complexity in the number of zero elements.

Since we don't know the size of the list, you should use the helper function in the template to access the value of the list at an index `i`; if `i` is too large for the list, the helper function returns `None`.

Because we don't know the length of the list, we only have one corner case, already in the doc-tests.

## 5: robot pathfinding with obstacles (25 points for MSFE; optional 5 points for MSAFA)

Use case: this is an interview question given to a colleague of yours last year.

A robot is located at the top-left corner of an `m x n` grid (i.e., at `(0, 0)`) and wants to reach the bottom-right corner (i.e., at `(m - 1, n - 1)`). However, there are obstacles in its way, and the robot can only move down or right at each step.

The function takes as argument a 2D list (i.e., a list of lists) representing the grid. The element at position `i, j` is `grid[i][j]`. The value is `True` if that position is open (or free), and `False` if it is closed (it has an obstacle). If a cell has an obstacle, the robot has to avoid it and cannot pass by that position. A grid is valid if it represents a real grid, and if the starting and ending positions are free. The function returns the number of distinct paths from start to finish (or 0, if there are none).

## 6: grid of numbers (30 points for MSFE only)

This function takes two arguments:

- an integer `number`

- a non-empty `grid` (or a matrix of numbers), represented as a list of lists (like the exercise on robot paths). The numbers in each row should strictly increase from left to right. The numbers in each column should strictly increase from top to bottom.

The function returns the indices `i, j` such that `grid[i][j] == number`, or `None` if `number` is not in the grid.

You should implement this function to run fast (i.e., do not check every number; instead, use the strict increasing order). Do not implement it in object-oriented programming (if you know about it).

Out of principle, in defensive programming, only check the type of the arguments (i.e., for the 2 corner cases already given in the doc-tests). Do not check that the grid contains only integers, nor that it is ordered; otherwise, we could just look for the number during that check.
