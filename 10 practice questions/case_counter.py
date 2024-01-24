"""
Letter Case Counter Function

Objective:
Write a function named 'case_counter' that counts the number of uppercase and lowercase letters in a given string. 数大小写

Function Parameter:
text (string): The string in which the letters need to be counted.

Instructions:
- The function should calculate and print two numbers: the count of uppercase letters and the count of lowercase letters in the string.
- If there are no letters of a particular case (uppercase or lowercase) in the string, the function should print 0 for that case. 特殊情况0
- Non-alphabetic characters in the string should be ignored and not counted. 非字母不计数

Example Test Cases:
1. case_counter("Hello World!") should print the counts of uppercase and lowercase letters.
2. case_counter("PYTHON") should print the counts of uppercase and lowercase letters.
3. case_counter("python") should print the counts of uppercase and lowercase letters.
4. case_counter("1234!@#$") should print 0 for both counts.
"""


def case_counter(text):
    # Your code goes here
    # Remember to count uppercase and lowercase letters and ignore non-alphabetic characters
    # pass  # Delete this after implementing some code inside this function.
    
    # initialize counters
    uppercase_count = 0
    lowercase_count = 0

    for char in text:
        # check if char is alphabet
        # 如果是字母
        if char.isalpha():
            # check uppercase
            if char.isupper():
                uppercase_count += 1
        # check lowercase
            elif char.islower():
                lowercase_count += 1

    print(f"Uppercase letters: {uppercase_count}, Lowercase letters: {lowercase_count}")



# Test cases
case_counter("Hello World!")  # Expected: Uppercase letters: 2, Lowercase letters: 8
case_counter("PYTHON")  # Expected: Uppercase letters: 6, Lowercase letters: 0
case_counter("python")  # Expected: Uppercase letters: 0, Lowercase letters: 6
case_counter("1234!@#$")  # Expected: Uppercase letters: 0, Lowercase letters: 0

case_counter("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz")  # Expected: Uppercase letters: 26, Lowercase letters: 26
case_counter("1! 1! 1! 1! 1! 1! 1! 1! 1! 1! 1! 1!")  # Expected: Uppercase letters: 0, Lowercase letters: 0
