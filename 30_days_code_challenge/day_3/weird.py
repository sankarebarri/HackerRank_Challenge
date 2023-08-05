"""
Task
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
Complete the stub code provided in your editor to print whether or not n is weird.
"""

def weird(n):
    if n >0:
        odd = (n%2 == 1)
        even = (n%2 == 0)
        if odd:
            print("Weird1") 
        elif even and (n >= 2 and n <= 5):
            print("NotWeird2")
        elif even and (n >= 6 and n <= 20):
            print("Weird3")
        else:
            print("Not Weird4")

print(weird(4)) # 
print(weird(5)) # weird1
print(weird(4)) # not weird2
print(weird(11)) # weird1
print(weird(16)) # weird3
print(weird(21)) # weird1
print(weird(28)) # not weird4