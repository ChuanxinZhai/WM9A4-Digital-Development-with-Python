"""
Compound Interest Calculator Function
利息计算
Objective:
Write a function named 'compound_interest_calculator' to calculate compound interest.

Function Parameters:
1. P (float): Principal amount.  本金
2. r (float): Annual interest rate in decimal.  年利率
3. n (integer): Number of times interest is compounded per year.  每年计算利息的次数
4. t (integer): Number of years for investment.  存款年数

Instructions:
- Use the formula: A = P(1 + r/n)^(nt) to calculate compound interest.
- Return the accumulated amount A after t years.
- Handle edge cases for inputs. 要解决边缘情况

Example Test Cases:
1. compound_interest_calculator(1000, 0.05, 12, 5) should calculate the amount.
2. compound_interest_calculator(500, 0.07, 4, 10) should calculate the amount.
3. compound_interest_calculator(1500, 0.03, 6, 7) should calculate the amount.
"""


def compound_interest_calculator(P, r, n, t):
    """
    本金P应该>0, 年利率r应该>0, 每年计算利息的次数应该大于0, 存款年数应该>=0;
    In real life cases, I think P should >0, no one will save money with negative amount and 0, and banks would not permit you to do like this.
                                r should >0; otherwise, it's not a interest, it's a debt. And I think r should <1, otherwise, it's not a normal interest.
                                n should >0 and should be an integer.
                                t should >=0 and should be an integer. 0 year means no interest.
    """

    # 否则返回Invalid input
    if P <= 0 or r <= 0 or r >= 1 or n <= 0 or t < 0:
        if r >= 1:
            return "Annual interest rate cannot be >= 1"
        return "Invalid input"
    if not isinstance(n, int):
        return "Please enter an integer for the number of compounding periods per year"
    if not isinstance(t, int):
        return "Please enter an integer for the number of years"

    # Calculate compound interest using the formula: A = P(1 + r/n)^(nt)  计算
    A = P * (1 + r / n) ** (n * t)
    return A


# Test cases
print(compound_interest_calculator(1000, 0.05, 12, 5))  # Expected: Amount after 5 years
print(compound_interest_calculator(500, 0.07, 4, 10))  # Expected: Amount after 10 years
print(compound_interest_calculator(1500, 0.03, 6, 7))  # Expected: Amount after 7 years

# Testing edge cases
print(compound_interest_calculator(0, 0.05, 12, 5))      # P = 0
print(compound_interest_calculator(-100, 0.05, 12, 5))   # P < 0
print(compound_interest_calculator(1000, -0.05, 12, 5))  # r < 0
print(compound_interest_calculator(1000, 0, 12, 5))      # r = 0
print(compound_interest_calculator(1000, 0.05, -1, 5))   # n < 0
print(compound_interest_calculator(1000, 0.05, 0, 5))    # n = 0
print(compound_interest_calculator(1000, 0.05, 2.5, 5))  # n = 2.5
print(compound_interest_calculator(1000, 0.05, 12, -1))  # t < 0
print(compound_interest_calculator(1000, 0.05, 12, 0))   # t = 0
print(compound_interest_calculator(1000, 0.05, 12, 0.5)) # half a year

print(compound_interest_calculator(1500, 1.2, 6, 7))    # r > 1
    
