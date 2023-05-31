import sys
from io import StringIO

test_input1 = '''3
ABC
DEF
X!@
!'''

sys.stdin = StringIO(test_input1)

n = int(input())

matrix = []
for _ in range(n):
    row = input()
    matrix.append(row)


searched = input()

# version 1
# is_found = False  # flag using
# for i in range(n):
#     if is_found:
#         break
#     for j in range(n):
#         if matrix[i][j] == searched:
#             print(f"({i}, {j})")
#             is_found = True
#             break

#version 2

for r in range(len(matrix)):
    if searched in matrix[r]:
        row = r
        col = matrix[r].index(searched)
        print(f"({r}, {col})")
        break
# input:
# 3
# ABC
# DEF
# X!@
# !
