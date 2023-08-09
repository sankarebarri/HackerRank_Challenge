"""
Task
Given an array, A,of N integers, print A's elements in reverse order as a single line of space-separated numbers.

Example
A = [1, 2, 3, 4]

Print 4 3 2 1. Each integer is separated by one space.
"""
a = [1,2,3,4]

a_r = ''
for i in a:
    a_r = str(i) + ' ' + a_r
    print(a_r)
print(a_r)