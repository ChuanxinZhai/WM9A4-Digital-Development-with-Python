# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

# Function to find the start and end indices of a substring in a string
def find_indices(S, k):
    # Initialize an empty list to store the start and end indices
    matches = []
    
    # Find all matches using a loop
    for match in re.finditer(r'(?={})'.format(re.escape(k)), S):
        # Since finditer does not include the end index of the match, we calculate it
        start_index = match.start()
        end_index = start_index + len(k) - 1
        matches.append((start_index, end_index))
    
    # Print the tuples if matches are found, otherwise print (-1, -1)
    if matches:
        for match in matches:
            print(match)
    else:
        print((-1, -1))

# Input format: Two lines, first the string S, then the substring k
if __name__ == '__main__':
    S = input().strip()
    k = input().strip()
    find_indices(S, k)
