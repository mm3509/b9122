---
title: 'Final exam (B9122, Computing for Business Research)'
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

# Final exam

You asked for more doc-tests, so Python questions now have 6 doc-tests.

Maximum comment share is 20%; except for debugging, where it's 100% (i.e., no limit).

Questions 1-9 are for MSFA only. Questions 11-19 are for MSFE only.

## 1: debugging dictionaries (MSAFA only, 10 points)

This function takes as input a UNI with letters and numbers, ensures that it is a valid UNI, and returns the program of that UNI, or `None` if the UNI is missing. For privacy, your UNIs have been truncated.

A UNI is valid if:

- it has at least 4 characters
- it has two parts only, the first consisting of only ASCII letters (uppercase or lowercase), the second consisting of only digits
- it has at least 2 letters and 2 numbers

The file has a bug and does not pass the doc-tests (the bug can be in the whole code, not just in the function). Find the bug, fix it, and add a comment explaining the bug.

## 2: merging lists (MSAFA only, 15 points)

This function merges two lists with unique integers in each, and returns a new list, keeping the order of the first list, adding at the end items from the second list (if missing from the first) in the order they appear.

Use case: you have presented a report for Q1 with an analysis of profitability by geographic region and in a certain order (e.g., decreasing importance). In Q2, the business has expanded to new regions. You want to present a Q2 report that is comparable side-by-side to Q1, so it has to maintain the order of regions in Q1 (even if absent from Q2) and then the order of regions in Q2. For simplicity, the regions are integers, and the result of a data analysis pipeline from some other Python program.

You can check if an item `element` is present in a list `list1` with this syntax: `if element in list1:`.

## 3: url to search terms (MSAFA only, 15 points)

Use case: you have a Python script that checks eBay every day with several search URLs, such as [this search URL](https://www.ebay.com/sch/i.html?_nkw=a+practical+guide&_saca=0). The page returns many items and you want to be notified of only those that match the search terms you used, such as "a practical guide" in this case, so you need to convert the search URL to a list of terms in the search, such as `['a', 'practical', 'guide']` in this case, to ignore items that don't have those terms.

This function takes one argument, a string with a search URL. It returns the search terms in the link, after the common prefixes defined in a global variable at the top of the file, until the character `&`. The character `&` is a delimiter for "GET paramters" in URLs; for example, if you passed included $10 as a maximum price in the search, the URL would contain something like `&_udhi=10`, where `_udhi` is some eBay syntax for the maximum price, see [here](https://www.ebay.com/sch/i.html?_nkw=a%20practical%20guide&_saca=0&rt=nc&_udhi=10)). You should also split the search terms by the character `+`, which is how eBay and some other websites represent a space in a URL.

The function returns a list of words of the search terms present in the search URL.

## 4: implementing the lowercase method (MSAFA only, 20 points)

This function implements the conversion of a string to lowercase, from the basics, without using `.lower()`. You should use `ord()` and `chr()`. Do not use a dictionary, or string methods `.lower()` or `.upper()`. Don't use `string.ascii_uppercase`, nor `string.ascii_lowercase`, nor `string.ascii_letters`.

In ASCII, the uppercase letters have ordinal 65 to 90 and lowercase letters have ordinal 97 to 122 (both in alphabetical order). You can see them [on Wikipedia](https://en.wikipedia.org/wiki/Ascii#ASCII-printable-characters).

For simplicity, the function should only accept strings where each character is represented by an ASCII number between 0 and 127 (7 bits).

## 5: orders of magnitude (MSAFA only, 20 points)

Use case: you want to measure the accuracy of a k-Nearest Neighbors model with varying `k` on the credit card fraud dataset. Running it for every `k` from 1 to 10 thousand would be too long, so we want to run it on `k` on a logarithmic scale, for example: 1, 2, 5, 10, 20, 50, 100, 200, 500.

This function takes two arguments:

- a list `leading` with unique integer digits, such as `[1, 2, 5]` or `[9, 8, 1]` (not necessarily sorted), representing the leading digit in `k`;

- a list `orders_magnitude` with two non-negative integers, such as `[1, 3]` or `[2, 0]` (not necessarily sorted), representing the starting and ending order of magnitude for the range of `k`.

The function returns a list of integers `k = i * 10 ^ j`, for `i` in `leading` and `min(orders_magnitude) <= j <= max(orders_magnitude)`, in increasing order.

Note: the body of the function is simple; the important part is the defensive programming with plenty of corner cases.

## 6: syllabification (MSAFA only, 20 points)

Use case: this is a linguistics problem, which you can solve with recursion.

"Syllabification" consists of arranging a word by syllables. The word "diamond" has two syllabifications: "di-a-mond" (3 syllables) or "dia-mond" (2 syllables). This exercise counts how many syllabifications are theoretically possible in a word of length `n`.

For simplicity, we only consider 3 types of syllables:

- a short syllable has 1 character (length 1);

- a medium syllable has 2 characters (length 2);

- a long syllable has 3 characters (length 3).

If we consider a word of length 2, it has 2 syllabifications: [short-short], and [medium].

If we consider a word of length 3, it has 4 syllabifications: [short-short-short], [short-medium], [medium-short], and [long].

This function takes as input a strictly positive integer representing the number of letters in a word. It returns the number of different syllabifications of that word (where syllables have length 1, 2 or 3).

## 7: textual question on kNN (MSAFA only, 15 points)

Please explain, at a high level, how you would apply k-Nearest Neighbors in the case of predicting earnings-per-share for a publicly traded company Z in 2026. You should target 1-3 paragraphs.

## 8: VBA question (MSAFA only, 15 points)

Write a VBA function to convert an interest rate from annual to daily, assuming 250 days in the year (similar to assignment 1). You do not need to round the answer to a certain number of digits.

You can test your VBA macro in Excel. But for Autograder, please copy-paste only the code from the macro into the empty template file. Do not submit a `.xlsx` nor a `.xlsm` file.

Since you don't have doc-tests nor Autograder, here are some sample inputs and outputs. They are taken from the solution code in assignment 1, rounded only for readability only. And I confirm that the output is correct for these inputs.

```
Annual rate: 0.10 <-> daily rate: 0.0004
Annual rate: 0.20 <-> daily rate: 0.0007
Annual rate: 0.30 <-> daily rate: 0.0011
Annual rate: 0.40 <-> daily rate: 0.0013
Annual rate: 0.50 <-> daily rate: 0.0016
Annual rate: 0.60 <-> daily rate: 0.0019
Annual rate: 0.70 <-> daily rate: 0.0021
Annual rate: 0.80 <-> daily rate: 0.0024
```

## 9: guest speaker question (MSAFA only, 10 points)

Please write a summary of 1-3 paragraphs, in your own words, of the guest speaker's career advice. You can either rephrase the general advice or write how it would apply to you in particular.

## 11: debugging (MSFE only, 10 points)

Use case: generating input data for one exercise in Autograder in assignment 4.

This function has 2 bugs. The function hits the "guardrail" assertions at the end (guardrail / failsafe assertions are different from defensive programming, and check the internal logic, and not the external arguments).

Find the 2 bugs, fix them, and add two comments explaining them.

## 12: orders of magnitude (MSFE only, 12 points)

Use case: you want to measure the accuracy of a k-Nearest Neighbors model with varying `k` on the credit card fraud dataset. Running it for every `k` from 1 to 10 thousand would be too long, so we want to run it on `k` on a logarithmic scale, for example: 1, 2, 5, 10, 20, 50, 100, 200, 500.

This function takes two arguments:

- a list `leading` with unique integer digits, such as `[1, 2, 5]` or `[9, 8, 1]` (not necessarily sorted), representing the leading digit in `k`;

- a list `orders_magnitude` with two non-negative integers, such as `[1, 3]` or `[2, 0]` (not necessarily sorted), representing the starting and ending order of magnitude for the range of `k`.

The function returns a list of integers `k = i * 10 ^ j`, for `i` in `leading` and `min(orders_magnitude) <= j <= max(orders_magnitude)`, in increasing order.

Note: the body of the function is simple; the important part is the defensive programming with plenty of corner cases.

## 13: syllabification (MSFE only, 10 points)

Use case: this is a linguistics problem, which you can solve with recursion.

"Syllabification" consists of arranging a word by syllables. The word "diamond" has two syllabifications: "di-a-mond" (3 syllables) or "dia-mond" (2 syllables). This exercise counts how many syllabifications are theoretically possible in a word of length `n`.

For simplicity, we only consider 3 types of syllables:

- a short syllable has 1 character (length 1);

- a medium syllable has 2 characters (length 2);

- a long syllable has 3 characters (length 3).

If we consider a word of length 2, it has 2 syllabifications: [short-short], and [medium].

If we consider a word of length 3, it has 4 syllabifications: [short-short-short], [short-medium], [medium-short], and [long].

This function takes as input a strictly positive integer representing the number of letters in a word. It returns the number of different syllabifications of that word (where syllables have length 1, 2 or 3).

## 14: invert a Markdown document (MSFE only, 12 points)

Markdown is my alternative to Word documents, and is also the format of this exam, of text files on GitHub, and of text cells on Jupyter Notebook. For simplicity, a Markdown file has to start with a heading (`# `), otherwise it's not a valid file.

Use case: You meet clients regularly and take notes in Markdown format, where a line starting with `# 15 October 2025` is a *heading*, and the lines after that (which don't start with `# `) are the contents from that meeting. When you started taking these notes, you added new meetings to the start of the file (most recent first, similar to a CRM like HubSpot). Now you changed systems and want to add new days to the bottom of the file (most recent last). To maintain a chronological order, you need to invert the order of your existing documents.

This function inverts a Markdown document by level-1 headings (which start with `# `): the last heading moves to the top, the second-to-last heading moves to second place, etc., and the first heading moves to the bottom.

Remember: like in two previous assignments, a newline in Python is denoted `\n`, but in doc-tests, the escape character `\` has to be escaped as well. Therefore, newlines in doc-strings appear as `\\n`, but if you copy the code in the doc-tests to the main script, then you have to replace `\\n` with `\n`.

If you want, you can remove empty newlines from the beginning and ending of the **original** document. To remove all newlines from the beginning and end of the argument `markdown`, use `markdown = markdown.strip("\n")`. This is already in the template file.

## 15: clean an object (MSFE only, 16 points)

Use case: you have a web server and a framework to collect user surveys. Sometimes, the framework adds an extraneous key-value pair in a dictionary, `"number": 0`, and you want to remove all of those.

This function takes as input any value (and therefore, has no defensive programming). If the value is a dictionary, it removes any key-value pair `"number": 0` from the dictionary. If the value is a list, it removes any key-value pair `"number": 0` from any dictionaries in that list.

This applies to nested objects too. For example, if a dictionary A has a value that is a list B, and that list B has a dictionary C with a key-value pair `"number": 0`, you should remove that key-value pair from dictionary C inside list B inside dictionary A.

Notes:

- The function works in-place, as shown in the doc-tests;

- To remove a key from a dictionary, use syntax `del adict[key]`, for example `del arg["number"]`;

- Python does not let you iterate through a dictionary and remove a key at the same time, so you should store the list of initial keys as shown in the template, then iterate on those.

## 16: generating an increasing grid, diagonally (MSFE only, 23 points)

This exercise has the same use case as exercise 11.

The code in exercise 11 works, but it is quite slow: inside each operation of the nested for loop, we save the value in the column above and the row to the left, and that the row and column are increasing. This adds four operations for each step of the nested for loop.

Another approach is to first generate the list of numbers, then distribute them in a grid. We could distribute them horizontally or vertically. But if so,the problem becomes similar to finding a number in a list sorted in one dimension, and Autograder could mark as correct a submission that works for these specific cases, but not for the general case of input data as in exercise 11.

Instead, we will distribute the numbers **diagonally**. If the list of numbers were `[1, 2, 3, 4]`, and the grid is `2 x 2`, then the grid would be:

```
[[1, 3],
 [2, 4]]
```

and now the grid is not sorted in any single dimension.

Complete the function to implement this procedure of distributing numbers diagonally.

## 17: linear regression and the CAPM (MSFE only, 17 points)

Use case: you want to find the stock that has the highest alpha on the CAPM, the stock with the highest sensitivity to the market, and the stock with the lowest sensitivity.

This function takes as input a list of ticker codes, such as `["AAPL", "GOOG", "MSFT"]`. It applies the CAPM to each of these ticker codes (restricting to the period of time with common data) and returns a triplet with the code for the highest `alpha`, the highest `beta`, and the lowest `beta`.

As we saw in lecture 9, the data for the risk-free rate and the market rate is already in a CSV file. The template file already downloads the data and prepares it for a CAPM regression. You have to add a linear regression for each ticker and keep track of the optimal stocks. You can use the code from the lecture and apply the required modifications.

Notes:

- this question on data analysis has no defensive programming;

- if you get an error such as `unexpected argument: multi_level_index`, upgrade to the latest version (`0.2.66`). If you're using Jupyter, you'll need to restart the kernel so it uses the version you just installed.

## 18: comparison of 3 classifiers (MSFE only, 35 points)

Use case #1: some of you want to write a thesis, for example building a model to predict stock quality (buy / hold / sell) for investment decision-making. This is the procedure to do so.

Note: this question on data analysis has no defensive programming.

We have covered 3 classifiers: k-nearest neighbors, logistic regression, and neural networks. In this exercise, you will apply these again to a variation of the credit card dataset (the same dataset as assignment 4 and lecture 12, which you can get from there).

The dataset had a huge imbalance: only 0.17% of transactions were fraudulent. After lecture 12, to check whether the method I presented had a problem, I started by "rebalancing" the dataset, and restricting legitimate transactions to a random sample with the same size as fraudulent transactions.

In this exercise, you will complete the Jupyter notebook already provided. This notebook contains code that rebalances the dataset in the last cell with code. You will have to write or copy the remaining cells with code (you can use the notebook from lecture 12), check the results, and write a text cell at the end with your conclusions.

The notebook provided follows the same procedure as lecture 12. After the last cell of code, each text cell has starts with `TODO`. You should add a code cell to perform the task in the previous text cell. You do not have to write text in these cells; you can save all of those for the last cell (which is text only).

In particular, you should:

- check a few rows of the data and compute summary statistics;

- plot the data;

- split the dataset into training, testing, and validation;

- estimate the three models, optimizing the hyperparameters if relevant (use the suggested possible values detailed in the notebook);

- compare the 3 classifiers with the accuracy score on the test dataset;

- complete the final text cell with a summary of the data analysis: what patterns did you find in the data; what is the best classifier, and why.

## 19: SQL (MSFE only, 5 points)

Visit SQLfiddle.com and click on `MySQL`. Copy the contents of `world.sql` into the SQL window, like we did in lecture 12 (remember that the database is transient), then add a query at the bottom to find the names of the countries from continents starting with the letter "A" where the population is over 100 million, sorted descendingly on population.

Copy the query only (a few lines, not the 5 thousand lines) into the template file.

You should see this result:

```
Name	Population
----------------------
China	1277558000
India	1013662000
Indonesia	212107000
Pakistan	156483000
Bangladesh	129155000
Japan	126714000
Nigeria	111506000
```
