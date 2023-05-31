import sys
from io import StringIO

test_input = '''2 3
1 2 3
4 5 6
swap 0 0 1 1
swap 10 9 8 7
swap 0 1 1 0
END'''

sys.stdin = StringIO(test_input)


def is_valid_position(rows, cows, r1, c1):
    if rows < 0 or cows < 0 or rows >= r1 or cows >= c1:
        return False
    return True


(r, c) = [int(x) for x in input().split(' ')]
matrix = []
for _ in range(r):
    matrix.append([int(x) for x in input().split(' ')])

while True:
    line = input()
    if line == 'END':
        break
    args = line.split()
    if args[0] != 'swap' or len(args) != 5:
        print('Invalid input')
        continue
    row1, col1, row2, col2 = [int(x) for x in args[1:]]
    if not is_valid_position(row1, col1, r, c) or not is_valid_position(row2, col2, r, c):
        print('Invalid input')
        continue
    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    for row_element in matrix:
        print(' '.join([str(x) for x in row_element]))
