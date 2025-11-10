# Assignment 4

This assignment contains two problems from LeetCode, one easy level, one medium level, to show that you are achieving the learning outcomes of solving LeetCode problems.

Data analysis exercises (6 and 7) are just a few lines of code. They do not require doc-tests nor defensive programming. Autograder inflates the other criteria to make 65% of the points for the exercise.

The maximum comment share for this exercise is 30%; for the debugging exercise, it's 90%.

## 1: debugging (15 points for MSFE, 30 points for MSAFA)

This function generates input test data for the midterm exercise on merging slides. It has a bug and throws an assertion error.

Find the bug, fix it, and add a comment explaining the bug.

Note: because of the random element, it's possible that you fix the bug but Autograder says that your results don't pass. If that happens to you, please mention it on Canvas Discussions and I will change the Autograder to accept your results.

## 2: majority element (15 points for MSFE, 30 points for MSAFA)

This exericse comes from LeetCode (easy level), with some modifications.

This function takes as input a list of strings of length `n` and returns the majority element. The majority element is the element that appears more than `int(n / 2)` times. If the majority element does not exist or is not unique, the function returns `None`.

Do not use `collections.Counter` (if you know about it).

## 3: triple sum (MSFE only, 25 points)

This exercise comes from LeetCode (medium level), with some modifications.

This function takes one argument, an array of integers `num`. It returns a list with all zero-sum triplet elements (not indices) of the original list. That is, each element of the return list is itself a list with 3 elements (a triplet), `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

The return list must not contain duplicate triplets (even if two different triplets satisfy the constraints above).

To simplify the doc-tests and testing on Autograder, each triplet must be sorted ascendingly (i.e. `[-1, -1, 2]`) and the list of triplets must be in "lexicographic" order. That is, if triplet `a` appears in the list before `b`, then `a[0] <= b[0]` (i.e. the first element of each triplet must be in ascending order); if the first elements are equal (`a[0] == b[0]`), then `a[1] <= b[1]` (i.e. the second elements must be in ascending order); if the first two elements in `a` and `b` are equal, then the third element is also equal and these two triplets are duplicates that should not be in the list.

First, implement a trivial algorithm in the first function, with at least cubic complexity (O(N^3)). That is, your algorithm can have 3 nested for loops.

Then, implement a faster version of the algorithm in the second function to pass the speed test. This function should have quadratic complexity (O(N^2)), i.e. at most 2 nested for loops. There are two tricks to optimize this function: the first is a shortcut to go from O(N^3) to O(N^2), and the second is a patch to avoid returning duplicated triplets without iterating through the list of triplets (which is of the order N!, factorial of N, because triplets are combinations of elements from the original list). The end of the file has code that, if you run it directly, will measure the time of your slow and fast functions in one specific example, for which you should find a 10x improvement.

## 4: Expense forecast (25 points for MSFE, 50 points for MSAFA)

This exercise, which we saw in class, emphasizes that the optimal prediction under squared loss is the conditional mean. You will have to compute this conditional mean directly, without applying a statistical model like linear regression or k-nearest neighbors.

Use case: Your company (or a client) has a record of past projects with expenses by month. The company is starting a new project, which will only be paid at the end (upon delivery). The mismatch between expenses and revenue represents a risk of a negative balance on its bank account. To avoid a negative balance, the company wants to predict expenses from this new project month-by-month. For simplicity, you have to spend the whole budget (no budget overruns).

For simplicity, each past project always has a duration that is a multiple or a divisor of the new project duration. That is, if the new project lasts 12 months, then past projects can last 6, 4, 3, or 2 months, or 24, 36, 48 months (etc). This verification is included in a corner case.

As mentioned in class, I suggest you proceed in three steps, detailed in each function:

The first function normalizes the budget of one past project to match the new project's budget.

The second function normalizes the duration of one past project (by stretching or shrinking it) to match the new project's duration. For specific details, see the doc-tests. (Hint: first compute a boolean to check if the project should be stretched or shrunk; then compute the multiplier by which it should be stretched or shrunk.)

The third function takes three arguments:

- a positive number with the budget of the new project

- a positive integer with the duration of the new project in months

- a list of past projects, where each project is a list of a certain non-constant length `n`, and the list has expenses from month 0 to month `n - 1`.

The third function should call the first two and return the average expense for each month (i.e., the mean conditional on month) across all past projects (normalized on both months and budget), without rounding.

## 5: Experimentation with linear regression (15 points for MSFE, 30 points for MSAFA)

Linear regression is the optimal predictor under some assumptions, such as a linear relationship between inputs and output. But when the relationship is not linear, linear regression can be a bad predictor.

The exercise provided generates data where the expenses are all in the first month or the last month. If you run `experiment_with_linear_regression.py`, you can see that linear regression is a poor fit for this data.

In this exploratory exercise, you will search for anoother counter-example to the optimality of linear regression. The example you find must be conceptually different from the one I provide (expenses at the beginning or the end) and from what we saw in class (linear regression not guaranteed to use exactly the duration, nor the exact budget).

Complete the file to generate input data, with code similar to the example helper function, but producing a different pattern.

After generating input data, run the Python file `experiment_with_linear_regression.py` to compare the results from linear regression to the results from the conditional mean. It will first plot my example data, the linear regression prediction, and your prediction from the previous exercise. When you close the plot, it will then plot your data and save your figure to a file `figure.png`.

Add a comment in the file explaining why linear regression does not make sense in the case of the data you generated. Also upload the figure to Gradescope without changing the filename (`linear-regression.png`).

## 6: k-Nearest Neighbors (MSFE only, 15 points)

This exercise and the next use the same dataset: a publicly available dataset on [credit card transactions](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud). For privacy reasons, the explanatory variables (`V1-V28`) in this dataset are obfuscated (they come from "dimensionality reduction" via Principal Components Analysis, and these are the most relevant factors). The other variables are the transaction amount and the label (1 for fraud, 0 for non-fraud). You need to unzip and extract the dataset in `creditcardfraud.zip`.

The function written loads the dataset, scales every feature (so they are comparable in Euclidean distance for k-nearest neighbors), and returns a sample of it as training data and test data.

To estimate a probability of fraud with k-nearest neighbors, we can choose `k` to be large and return the proportion of neighbors that are labeled fraudulent. For example, if `k = 100`, we count how many of the nearest 10 neighbor transactions are fraudulent (say, 4 neighbors have this label), and then the probability of fraud is 4%. SciKit-Learn does this with the method `.predict_proba()`.

Complete the function to return the probability that a new transaction is fraudulent.

The function takes two inputs, a value for `k` and a list of numbers (one value for each feature), and returns one output, a float with a probability between 0 and 1.

## 7: logistic regression / classification (MSFE only, 15 points)

With the same dataset, complete the function to predict the probability of fraud using logistic regression.

The function takes one input, a list of numbers (one value for each feature), and returns one output, a float with a probability between 0 and 1.

## 8: comparison of kNN and logistic regressions (MSFE only, 15 points)

Adapt the code at the bottom of the two previous files to inspect some of the predicted probabilities from kNN (for some `k` around 100) and logistic regression.

Which model is more appropriate for this dataset of fraudulent transactions?

Submit your answer as `exercise_8_comparison.txt`.
