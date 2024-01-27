"""
Fibonacci Sequence Calculator Function
斐波那契数列
Objective:
Write a function named 'fibonacci_sequence' to generate the Fibonacci sequence up to a given number using a while loop. 使用while循环写一个生成斐波那契数列的函数

Function Parameter:
1. max_value (integer): Maximum value for the Fibonacci sequence.

Instructions:
- Use a while loop to generate the Fibonacci sequence up to 'max_value'.
- Return the sequence as a list. 返回一个列表
- Handle edge cases for 0 and negative inputs.

Example Test Cases:
1. fibonacci_sequence(10) should return the Fibonacci sequence up to 10.
2. fibonacci_sequence(1) should return the Fibonacci sequence up to 1.
3. fibonacci_sequence(0) should return a sequence with 0.
4. fibonacci_sequence(-5) should handle negative input.
"""


def fibonacci_sequence(max_value):
    # <0

    if not isinstance(max_value, int) or max_value < 0:
        # for normal fibonacci sequence, it should be an interger (not float)
        return "Invalid input: max_value must be a non-negative integer"

    # Initialize Fibonacci sequence
    sequence = [0]

    # = 0 
    if max_value == 0:
        return sequence

    # 添加第二个元素
    sequence.append(1)


    while True:
        next_value = sequence[-1] + sequence[-2]
        if next_value > max_value:
            break
        sequence.append(next_value)

    return sequence


# Test cases
print(fibonacci_sequence(10))  # Expected output: [0, 1, 1, 2, 3, 5, 8]
print(fibonacci_sequence(1))  # Expected output: [0, 1, 1]
print(fibonacci_sequence(0))  # Expected output: [0]
print(fibonacci_sequence(-5))  # Expected: Empty list or error message
# test float numbers
print(fibonacci_sequence(-1.5))
print(fibonacci_sequence(5.5))
