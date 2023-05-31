import sys
from io import StringIO

test_input = '''3
1 2 3
4 5 6
7 8 9
Add 0 0 5
Subtract 1 1 2
END'''

sys.stdin = StringIO(test_input)

def is_valid_coordinates(row, col, number):
    if row < 0 or col < 0 or row >= number or col >= number:
        return False
    return True


matrix = []
n = int(input())
for i in range(n):
    matrix.append([int(x) for x in input().split(' ')])

while True:
    line = input()
    if line == 'END':
        break
    command = line.split(' ')

    r, c, num = [int(x) for x in command[1:]]
    if not is_valid_coordinates(r, c, n):
        print('Invalid coordinates')
        continue

    if command[0] == 'Add':
        matrix[r][c] += num
    elif command[0] == 'Subtract':
        matrix[r][c] -= num


for k in range(len(matrix)):
    print(' '.join([str(x) for x in matrix[k]]))
