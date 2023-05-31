# write program that read matrix
# print sum of all nums in it
# print the matrix


def read_matrix():
    (n, m) = [int(x) for x in input().split(', ')]  # unpacking tips

    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)
    return matrix


matrix = read_matrix()
r = len(matrix)
c = len(matrix[0])
the_sum = 0

for row_index in range(r):
    row = matrix[row_index]
    the_sum += sum(row)
    # for col_index in range(c):
    #     the_sum += row[col_index]

print(the_sum)
for r in matrix:
    print(r)

# input:
# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0
