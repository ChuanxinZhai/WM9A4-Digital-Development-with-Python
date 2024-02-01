
S, k = input().split()
k = int(k)


permutations_list = list(permutations(S, k))


for p in sorted(permutations_list):
    print("".join(p))
