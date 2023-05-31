# input will be matrix sizes and data
# print nem matrix only with the even numbers
import sys

data_input = """2, 3
1, 2, 3
4, 5, 6"""


def read_matrix():
    (n, m) = [int(x) for x in input().split(', ')]  # unpacking tips

    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)
    return matrix


matrix = read_matrix()

# version 1
# r = len(matrix)
# c = len(matrix[0])
# for i in range(r):
#     row = matrix[i]
#     for j in range(c-1, -1, -1):
#         if not row[j] % 2 == 0:
#             del row[j]
#
# print(matrix)

# version 2 :D
only_even = []
for row in matrix:
    only_even = [x for x in row if x % 2 == 0]
    print(only_even)
