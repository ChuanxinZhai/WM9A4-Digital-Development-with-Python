"""
Factorial Calculator Function
阶乘
Objective:
Write a function named 'calculate_factorial' to compute the factorial of a number using a for loop. 用循环写一个计算阶乘的函数

Function Parameter:
1. number (integer): A non-negative integer for which the factorial is to be calculated. 
    非负整数
Instructions:
- Use a for loop to calculate the factorial of 'number'.
- Return the factorial result.
- Handle edge cases for 0 and negative inputs.

Example Test Cases:
1. calculate_factorial(5) should return the factorial of 5.
2. calculate_factorial(0) should return 1.
3. calculate_factorial(3) should return the factorial of 3.
4. calculate_factorial(-1) should handle negative input.
"""


def calculate_factorial(number):
    # <0
    if number < 0:
        return "Invalid input: number must be non-negative"

    # = 0  0的阶乘是1
    if number == 0:
        return 1

    # Calculate factorial using a for loop
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial


# Test cases
print(calculate_factorial(5))  # Expected output: 120
print(calculate_factorial(0))  # Expected output: 1
print(calculate_factorial(3))  # Expected output: 6
print(calculate_factorial(-1))  # Expected: Error message or specific value
print(calculate_factorial(1))
print(calculate_factorial(2))
print(calculate_factorial(9)) 
