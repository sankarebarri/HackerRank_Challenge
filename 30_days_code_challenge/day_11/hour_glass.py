"https://www.hackerrank.com/challenges/30-2d-arrays/problem?isFullScreen=false"

# A = [
#     [91, 1, 0, 1, 6],
#     [2, 1, 0, 1, 3],
#     [4, 1, 0, 1, 4],
#     [5, 4, 6, 9, 7],
#     [2, 1, 1000, 1, 3],
# ]
# A = [
#     [1, 1, 1, 0, 0, 0],
#     [0, 1, 0, 0, 0, 0],
#     [1, 1, 1, 0, 0, 0],
#     [0, 0, 2, 4, 4, 0],
#     [0, 0, 0, 2, 0, 0],
#     [0, 0, 1, 2, 4, 0]
# ]
# A = [
#     [0, -4, -6, 0, -7, -6],
#     [-1, -2, -6, -8, -3, -1],
#     [-8, -4, -2, -8, -8, -6],
#     [-3, -1, -2, -5, -7, -4],
#     [-3, -5, -3, -6, -6, -6],
#     [-3, -6, 0, -8, -6, -7]
# ]

A = []
# for _ in range(6):
#     A.append(list(map(int, input().rstrip().split())))

# print(A)

i = 3
final_biggest_sum = float("-inf")
for x in range(len(A)-2):
    j = 0
    move_left = 3
    biggest_sum = float("-inf")
    for k in range(len(A[1])-2):
        row_count = 0
        hour_glass_sum = 0  # initialize minimun sum, to avoid creating a list
        for a in A[x:i]:
            z = a[j+k:move_left+k]
            if row_count == 1:
                z[0] = 0
                z[2] = 0
            print(z)
            row_count += 1
            row_sum = sum(z)
            print("sum of rows of hour glass", row_sum)
            print("####")
            hour_glass_sum += row_sum
        print("sum of one hour glass", hour_glass_sum)
        print("###")
        if hour_glass_sum > biggest_sum:
            biggest_sum = hour_glass_sum

        print("####")
        print("if last hour gas sum greater than last hour glass", biggest_sum)
    if biggest_sum > final_biggest_sum:
        final_biggest_sum = biggest_sum
    print("the first loop of the outest loop", final_biggest_sum)
    # print(final_biggest_sum)

    move_left += 1
    j += 1
    i += 1
print(final_biggest_sum)
