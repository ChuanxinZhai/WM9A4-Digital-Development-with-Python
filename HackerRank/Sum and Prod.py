# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

# N, M
N, M = map(int, input().split())

array_elements = []

# read
for _ in range(N):
    row = list(map(int, input().split()))
    array_elements.append(row)

#  NumPy(np)
my_array = np.array(array_elements)

# sum
sum_result = np.sum(my_array, axis=0)


product_result = np.prod(sum_result)
print(product_result)
