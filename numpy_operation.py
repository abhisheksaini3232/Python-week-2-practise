import time
import numpy as np

numbers = np.arange(100000000)
start = time.time()
result = numbers * numbers
end = time.time()
print("NumPy execution time:", end - start)

'''output:
List execution time:0.20038652420043945
'''
#cpu usage: ~ 0%
# memory usage 1000 mb