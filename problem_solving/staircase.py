# https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

"""
Staircase detail

This is a staircase of size :

   #
  ##
 ###
####
Its base and height are both equal to . It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size .

Function Description

Complete the staircase function in the editor below.

staircase has the following parameter(s):

int n: an integer Print

Print a staircase as described above.

Input Format

A single integer, n , denoting the size of the staircase.

Constraints

0 < n <= 100
"""


def staircase(n):
    space = n - 1
    for i in range(1, 7):
        print(" "*space+"#"*i)
        space -= 1
