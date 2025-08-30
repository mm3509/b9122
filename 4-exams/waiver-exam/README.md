# Waiver / exemption exam

These exercises cover the four languages we learn in the course: Bash, SQL, C, and Python (which we learn in more depth and thus has more exercises). They are ordered by language, not by difficulty. You can solve them independently, e.g. if you get stuck in one question, move on to the next.

You will need to submit your answers on Gradescope, not on Canvas. You will get an automatic grade, which serves as a reference: we may adjust scores afterward if needed. Although this is a new tool for you, Autograder isn't hard to understand and a big part of coding is the ability to quickly adapt to and learn new tools and technologies.

Exercise 6 has examples of defensive programming, i.e. the doc-tests and the code anticipate corner cases in the arguments. For full credit, you will need to apply defensive programming in doc-tests and in code to the other Python exercises (4, 5 and 7), even though AutoGrader will only show the result of that grade after the due date.

You may not use any AI tools (chatbot, code completion, Google Search, etc); if you use AI tools, you will lose twice the points in the question, which almost surely implies that you will fail the exam.

## 1: Bash exercise (10 points)

Write a Bash or Zsh script that adds a prefix `b9122-` to every PDF file in the current directory. You can assume that at least one PDF file exists.


You can test it in the Terminal application on `macOS`, or by installing `git bash` on Windows.

## 2: SQL exercise (15 points)

The file `world.sql` contains a database of countries with tables `country` and `countrylanguage`.

Write an SQL query that retrieves the names of all the African countries where English is an oficial language and have 1 million or more in population.

Example output:

```
Name
Lesotho
South Africa
Zimbabwe
```

Notes:

- if you have SQL installed on your machine, load the `world.sql` file into it (e.g., by running in a shell `mysql -u USER -p DATABASE_NAME < PATH/TO/FILE.sql`)

- if you do not have SQL installed on your machine, use the website `sqlfiddle.com`, choosing `MySQL`, pasting the contents of the file `world.sql` into the text box, and adding your query at the end (the website does not keep memory of previous databases, so you have to load the database every time).

## 3: C exercise (25 points)

A prime number is a number that is only divisible by itself and the number 1. It has no other divisors. By convention, the number 1 is not a prime number.

The function in `exercise_3_c.py` returns the list of prime numbers from `2` to `n` using the fast method of the ["Sieve of Erathostenes"](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes). Convert this code from Python into C the function in `exercise_3_c.c`.

Example output:

```
List of primes until 11:
2
3
5
7
11
```

Note:

- if you do not have a C compiler installed on your machine, you can use an online compiler to test your code, e.g. at https://www.onlinegdb.com/online_c_compiler (choose `C` as the language at the top right).

## 4-7: Python exercises (90 points)

In all these exercises, you can gauge whether your code is correct by running the file in a shell (e.g., `python3 exercise_4_excel.py`): if you see no output, then your code passes the doc-tests. You may not modify any doc-test.

### 4: Excel column letters to number (10 points)

This exercise converts Excel column letters into numbers.

Complete the function and add defensive programming doc-tests in `exercise_4_excel.py` to pass the doc-tests. You may not use external libraries like `openpyxl`.

### 5: number to Excel column letters (10 points)

This exercise is the reverse of the previous exercise and converts numbers into Excel column letters.

Complete the function and add defensive programming doc-tests in `exercise_5_excel.py` to pass the doc-tests. You may not use external libraries like `openpyxl`.

### 6: Debugging (20 points)

The function in file `exercise_6_debug.py` takes a list of transactions and a list of keys. It returns a dictionary where each transaction in the first argument is allocated to a dictionary key in the second argument.

For example, each transaction in the first argument is a tuple with details on buying and selling shares; and the second argument is a list of ticker codes. The return value, transactions allocated by ticker code, serves to later compute the profitability of buying and selling one particular stock.

The function has a bug and does not pass the doc-tests. Find the bug and fix it, so the file passes the doc-tests. Also complete the text file `exercise_6_debug.txt`, explaining the bug and how you fixed it.

### 7: Numbers to words (50 points)

Most people use birthdays or birth years as PINs (personal identification numbers), which are insecure but easy to remember. The most secure PINs are random, but hard to remember. This exercise converts a random PIN into a word, which is easier to remember than a number, thus getting both advantages (secure and easy-to-remember).

Here is one intuitive correspondence of digits to letters:

- 1 is T or D because they have 1 downstroke

- 2 is N because it has 2 downstrokes

- 3 is M because it has 3 downstrokes

- and so on, as detailed in the file `exercise_7_pin.py`.

The remaining letters without correspondence, such as vowels, are ignored. Thus, the word `dynamo` encodes the number `123`: D is 1, N is 2, M is 3, and the letters without a correspondence (Y, A, and O) are ignored.

In this exercise, you'll implement three steps:

- convert an English word to a number, according to the correspondence above;

- from a list of all English words and the above function, and build a dictionary where a number is associated with a list of words that match that number;

- taking a number as input and with the above dictionary, return the list of all English words that match that number.

The file `exercise_7_pin.py` has a class `Converter` and methods that implement these steps. Add defensive programming doc-tests and complete the methods marked with `# TODO` to pass the doc-tests.

Note:

- use the variable `ENGLISH_WORDS_FILEPATH`, defined at the top of the file, to load the file with English words (instead of `english.txt`, because Autograder runs your code from a different directory)
