import numpy as np

# Read input
N, M, P = map(int, input().split())

# Initialize arrays
array_N = []
array_M = []

# Read elements for array N
for _ in range(N):
    row = list(map(int, input().split()))
    array_N.append(row)

# Read elements for array M
for _ in range(M):
    row = list(map(int, input().split()))
    array_M.append(row)

# Convert arrays to NumPy arrays
np_array_N = np.array(array_N)
np_array_M = np.array(array_M)

# Concatenate arrays along axis 0
result = np.concatenate((np_array_N, np_array_M), axis=0)

# Print the concatenated array
print(result)
