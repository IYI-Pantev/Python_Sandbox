# set bit(1) at position p
p = 5
n = 125
n_as_binary = bin(n)
print(n_as_binary)

mask = 1 << p
result = n | mask
result_as_binary = bin(result)
print(result_as_binary)