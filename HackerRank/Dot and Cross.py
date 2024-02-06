N = int(input())


A_elements = []
B_elements = []

# A matrix element
for _ in range(N):
    row = list(map(int, input().split()))
    A_elements.append(row)

# B matrix element
for _ in range(N):
    row = list(map(int, input().split()))
    B_elements.append(row)

# transport Numpy
A = np.array(A_elements)
B = np.array(B_elements)


print(np.dot(A, B))
