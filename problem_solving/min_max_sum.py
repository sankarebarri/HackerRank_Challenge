# https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

arr = [1,3,5,7,9]

Example
The minimum sum is 1 + 3 + 5 + 7 = 16 and the maximum sum is 3 + 5 + 7 + 9 = 24. 
 the function prints 16 24 .

Function Description

Complete the miniMaxSum function in the editor below.

miniMaxSum has the following parameter(s):

    arr: an array of  5 integers

Print Print two space-separated integers on one line: the minimum sum and the maximum sum of 4 of 5 elements. 

Input Format

A single line of five space-separated integers.

Constraints
1 <= arr[i] <=10^9
"""


def min_max_sum(arr):
    min_arr_sum = sum(arr[:5])
    max_arr_sum = sum(arr[-5:])

    return (min_arr_sum, max_arr_sum)
