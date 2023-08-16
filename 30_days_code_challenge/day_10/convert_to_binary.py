"""
Task
Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer 
denoting the maximum number of consecutive 1's in n's binary representation. When working with 
different bases, it is common to show the base as a subscript.

Example
n=25
The binary representation of 125 base 10  is 1111101. In base 10, there are 5 and 1 consecutive ones in two groups. Print the maximum, 5.
"""

def convert_to_binary(n):
    """
    Convert from base 10 to base 2
    n: postive integer

    Return: 1s and 0s -> i.e Base 2 representaion of the n
    """
    op_n = n
    remainder_list = []
    
    while op_n != 1 and op_n != 0:
        remainder = op_n % 2
        remainder_list.append(remainder)
        op_n = op_n // 2
        if op_n == 1:
            remainder_list.append(1)

    return remainder_list


def count_first_1s(n):
    """
    Keeps count of the consecutive 1s
    n: positive integer only in base 10

    Return: The maximum count of the consecutive 1s
    """
    count = 0
    ones_count = []

    # called the convert_to_binary function() above
    result = convert_to_binary(n)

    for res in result:
        if res == 1:            
            count += 1
        else:
            ones_count.append(count)
            count = 0
    ones_count.append(count)
    
    return max(ones_count)

