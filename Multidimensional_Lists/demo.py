basic = [1, 2, 3, 4]

print(basic[2])

ll = [
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5],
]

print(ll[2][0])

r = 5
c = 4

# for _ in range(r):
#     row = []
#     matrix_of_zeroes.append(row)
#     for _ in range(c):
#         row.append(0)
# version 2
# for _ in range(r):
#     row = [0] * c
#     matrix_of_zeroes.append(row)

# version 3
# matrix_of_zeroes = [[0] * c for _ in range(r)]
#
# [print(row) for row in matrix_of_zeroes]

# version 4
matrix = []
for i in range(3):
    matrix.append([])
    for j in range(1, 4):
        matrix[i].append(j)

    print(matrix[i])


