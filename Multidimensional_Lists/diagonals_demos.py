matrix = [
    [3, 15, 6, 18, 8],
    [8, 19, 20, 21, 30],
    [30, 11, 7, 9, 10],
    [8, 7, 4, 5, 3],
    [19, 20, 13, 14, 5]
]
r = len(matrix)
c = len(matrix[0])
n = 5
#   Primary diagonal
print('---Primary diagonal---')
print(
    [matrix[i][i] for i in range(n)]
)

# Secondary diagonal
# len(rows) - index - 1
print('---Secondary diagonal---')
print(
    [matrix[i][n - i - 1] for i in range(n)]
)

# Below primary diagonal
print('---Below primary diagonal---')
below_primary_diagonal = []
for i in range(r):
    for j in range(i):
        below_primary_diagonal.append(matrix[i][j])

print(below_primary_diagonal)

# above primary diagonal
print('---Above primary diagonal---')
above_primary_diagonal = []
for i in range(r):
    for j in range(i + 1, r):
        above_primary_diagonal.append(matrix[i][j])

print(above_primary_diagonal)

print('---Below secondary diagonal---')

below_secondary_diagonal = []
for i in range(r):
    for j in range(r-i, r):
        below_secondary_diagonal.append(matrix[i][j])

print(below_secondary_diagonal)

# above secondary diagonal
print('---Above secondary diagonal---')
above_secondary_diagonal = []
for i in range(r):
    for j in range(r-i-1):
        above_secondary_diagonal.append(matrix[i][j])

print(above_secondary_diagonal)