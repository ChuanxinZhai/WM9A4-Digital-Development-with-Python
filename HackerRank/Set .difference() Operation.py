# Enter your code here. Read input from STDIN. Print output to STDOUT



n_english = int(input())
english_subscribers = set(map(int, input().split()))


n_french = int(input())
french_subscribers = set(map(int, input().split()))


english_only_subscribers = english_subscribers.difference(french_subscribers)


print(len(english_only_subscribers))
