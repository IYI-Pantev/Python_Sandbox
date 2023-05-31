# read matrix - print diagonals and their sum

import sys
from io import StringIO

test_input = '''3
1, 2, 3
4, 5, 6
7, 8, 9'''

sys.stdin = StringIO(test_input)

n = int(input())

matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split(', ')])

primary_diagonal = []
for i in range(n):
    primary_diagonal.append(matrix[i][i])

print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")

secondary_diagonal = []
for j in range(n):
    secondary_diagonal.append(matrix[j][n-j-1])

print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")

