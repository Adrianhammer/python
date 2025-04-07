import random
import time
import numpy as np

num = 2_000_000
y = 0

start_time = time.time()
for i in range(num):
    x = random.uniform(0,1)
    y += x

print(f"Runtime: {time.time() - start_time:.4f} seconds")


numpy_start_time = time.time()
numpy_random = np.random.uniform(0, 1, num)
np.sum(numpy_random)
print(f"Runtime: {time.time() - numpy_start_time:.4f} seconds")
