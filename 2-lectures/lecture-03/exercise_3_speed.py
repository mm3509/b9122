# From Miguel: Ignore lines with the "time" module.
import time


integer_list = []
N = 100000  # Alternatively: N = int(1e5)

start = time.time()
for i in range(N):
    integer_list = [i] + integer_list  # ~ 11 seconds


elapsed_seconds = time.time() - start
print(f"Your code took {elapsed_seconds:.5f} seconds")
