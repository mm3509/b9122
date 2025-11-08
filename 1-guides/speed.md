# Speed

If Autograder flags your code for slowness, please read this document: it provides some examples to make your code run faster.

## Use native operations

As seen in lecture 2, some methods are faster than others, and I list them here:

- instead of `.insert(0, ...)`, change your logic to use `.append()`

## Use lists instead of strings

As seen in lecture 5, strings are immutable and any operation on them requires copying the whole list. If you change it to a list instead, your code runs faster.

Here is an example of adding letters to a string or to a list, where using a list makes the code 2.5 times faster:

``` python

import time
import string

def string_operation():
  long_string = ""
  for i in string.ascii_letters:
    long_string += i + " "
  return long_string

def list_operation():
  long_list = []
  for i in string.ascii_letters:
    long_list.append(i)
  long_string = " ".join(long_list)
  return long_string


N = int(1e4)
start = time.time()
for _ in range(N):
  string_operation()
string_duration = time.time() - start

start = time.time()
for _ in range(N):
  list_operation()
list_duration = time.time() - start


print("List manipulation: ", list_duration, ", strings:", string_duration)
print("Speed improvement:",  round(string_duration / list_duration, 2))

# This prints:
# List manipulation:  0.022916555404663086 , strings: 0.056812286376953125
# Speed improvement: 2.48
```

## Use sorting

If you need to return a list of unique elements, sorting can increase your speed. For the purpose of demonstration, consider this function that extracts the unique elements from a list of integers (without using sets):

``` python
def unique_elements(alist):

    assert isinstance(alist, list)
    assert all([isinstance(element, int) for element in alist])

    new_list = []
    for element in alist:
        if element in new_list:
            continue
        new_list.append(element)
        
    return new_list
```

This code is slow on long lists because it checks every element against all previous elements, and so has quadratic complexity.

If we sort before, we can improve the speed and the complexity because we only need to check the new element against the last element in the list, not all elements. The complexity is O(n log n) for sorting, and linear for the for loop, and therefore O(n log n) (which is better than quadratic).

``` python
def unique_elements(alist):

    assert isinstance(alist, list)
    assert all([isinstance(element, int) for element in alist])

    # This uses `sorted()` instead to `.sort()` to avoid changing the argument
    # in-place, creating a new local variable instead.
    alist = sorted(alist)
    
    new_list = []
    for element in alist:
        if element == new_list[-1]:
            continue
        new_list.append(element)
        
    return new_list
```
