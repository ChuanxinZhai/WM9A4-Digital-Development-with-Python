"""
Prime Number Checker Function
素数检查器
Objective:
Write a function named 'is_prime' to determine whether a given number is a prime number.

Function Parameter:
number (integer): The number to be checked for primality.

Instructions:
- The function should return 'True' if the 'number' is a prime number and 'False' otherwise.
True是素数, False不是素数
- A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
- Consider edge cases, such as when the input is less than 2, which is not a prime number. 边界情况
- https://mathspar.com/prime-numbers/#how-to-tell-if-a-number-is-prime

Example Test Cases:
1. is_prime(11) should return 'True', as 11 is a prime number.
2. is_prime(4) should return 'False', as 4 is not a prime number.
3. is_prime(2) should return 'True', as 2 is a prime number.
4. is_prime(1) should return 'False', as 1 is not considered a prime number.
"""

import math

def is_prime(number):
    # Your code goes here
    # Implement the logic to determine if the number is prime
    # Return True if the number is prime, False otherwise

    # Check if the input is a number (integer or float)
    if not isinstance(number, (int, float)):
        return False

    # Convert float to integer if it's a whole number, return False otherwise
    if isinstance(number, float):
        if number.is_integer():
            number = int(number)
        else:
            return False
    
    # Check if number is less than 2, not a prime number
    if number < 2:
        return False
    
    # 2 is the only even prime number
    if number == 2:
        return True

    # Exclude even numbers greater than 2
    if number % 2 == 0:
        return False

    # Check for factors up to the square root of the number
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    
    return True

print("Test basic cases:")
print(is_prime(11))  # Expected output: True
print(is_prime(4))  # Expected output: False
print(is_prime(2))  # Expected output: True
print(is_prime(1))  # Expected output: False
print(is_prime(0))  # Expected output: False
# long number
print(is_prime(32131241))
print(is_prime(3213124245423419))

print("-" * 35)  # Separator

print("Test floats:")
print(is_prime(0.0)) # Expected output: False
print(is_prime(1.0)) # Expected output: False
print(is_prime(1.5)) # Expected output: False
print(is_prime(2.0)) # Expected output: True
print(is_prime(2.5)) # Expected output: False
print(is_prime(3.0)) # Expected output: True
print(is_prime(23.0)) # Expected output: True
print("-" * 35)  # Separator


print("Test non-numeric and special cases:")
print(is_prime(math.pi))  # Expected output: False, as π is not an integer
print(is_prime(math.e))   # Expected output: False, as e is not an integer
print(is_prime("abcd"))  # Expected output: False
print(is_prime(",.!@")) # Expected output: False
print("-" * 35)  # Separator
