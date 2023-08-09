"""
Task
Given a string, , of length  that is indexed from  to , print its even-indexed and odd-indexed characters as  space-separated strings on a single line (see the Sample below for more detail).

Note:  is considered to be an even index.
"""
s = 'abcdef'
# 0,1,2,3,4
o_s = ''
e_s = ''

T = int(input().strip())
for i in range(0, T):
    for i in range(len(s)):
        even = (i%2==0)
        odd = (i%2==1)
        if even:
            e_s += s[i]
        else:
            o_s += s[i]

        print(f"{e_s} {o_s}")

# better code
for i in range(0, T):
    print(s[0::2], s[1::2])
