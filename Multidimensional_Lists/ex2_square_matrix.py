import sys
from io import StringIO

test_input = '''3 4
A B B D
E B B B
I J B B'''

sys.stdin = StringIO(test_input)


(r, c) = [int(x) for x in input().split(' ')]
matrix = []
for i in range(r):
    matrix.append(input().split(' '))
count = 0
for i in range(r-1):
    for j in range(c-1):
        if matrix[i][j] == matrix[i][j+1] == matrix[i+1][j] == matrix[i+1][j+1]:
            count += 1


print(count)