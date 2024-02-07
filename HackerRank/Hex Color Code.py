# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

# Regular expression
regex_pattern = r"(#[0-9a-fA-F]{3,6})[^\n ]"

N = int(input())

for _ in range(N):
    line = input()
    matches = re.findall(regex_pattern, line)
    for match in matches:
        print(match)
