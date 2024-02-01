# Enter your code here. Read input from STDIN. Print output to STDOUT


N = int(input())


distinct_stamps = set()


for _ in range(N):
    country = input()
    distinct_stamps.add(country)


print(len(distinct_stamps))
