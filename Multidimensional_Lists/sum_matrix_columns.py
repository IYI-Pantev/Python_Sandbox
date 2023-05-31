# reads matrix
# prints sum of each column

def read_matrix():
    (n, m) = [int(x) for x in input().split(', ')]  # unpacking tips

    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)
    return matrix


matrix = read_matrix()
columns = len(matrix[0])
rows = len(matrix)

# first version
# for i in range(columns):
#     sum = 0
#     for j in range(rows):
#         sum += matrix[j][i]
#     print(sum)

# second version

column_sums = [0] * columns
for i in range(rows):
    for j in range(columns):
        value = matrix[i][j]
        column_sums[j] += value

print(column_sums)