# From Miguel: Ignore lines with the "time" module.
import time 


integer_list = []
N = 100000  # Alternatively: N = int(1e5)

start = time.time()

"""
# From Miguel: This is a multi-line comment to show alternative
# solutions.


# Initial solution: loop in the correct order and insert at the beginning:
# around 11 seconds.
for i in range(N):
    integer_list = [i] + integer_list

# Improvement: use `.insert()` instead of +: around 2 seconds.
for i in range(N):
    integer_list.insert(0, i)

# No improvement: loop in reverse order and use +: around 11 seconds
for i in range(N, -1, -1):
    integer_list = integer_list + [i]
"""

# Best solution: use `.append()`: 0.003 seconds.
for i in range(N, -1, -1):
    integer_list.append(i)

    
elapsed_seconds = time.time() - start
print(f"Your code took {elapsed_seconds:.5f} seconds")
