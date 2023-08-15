"""
Complete the factorial function in the editor below. Be sure to use recursion.

factorial has the following paramter:

int n: an integer
Returns nx(n-1)x(n-2)x...x1

int: the factorial of 
Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of .

Input Format

A single integer, n (the argument to pass to factorial).
"""
def factorial(n):
    # Write your code here
    if n== 0:
        return 1
    return n*factorial(n-1)