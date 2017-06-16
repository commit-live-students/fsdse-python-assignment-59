"""
Write a function to find numbers divisible by two numbers.
Define a function that takes 3 parameters(all positive integers) in this order: num1, num2, end_num
Function should return a list of all numbers less than end_num that are divisible by both num1 and num2.
Example:

Input:

2, 3, 13
Output:

[6, 12]
Challenge: Write the function without using for-loop.
"""

def solution(num1, num2, end_num):
    """Enter Code Here"""
    if num1 > 0 and num2 > 0 and end_num > 0:
        x = [x for x in range(1,end_num+1) if x%num1==0 and x%num2==0]

    return x
