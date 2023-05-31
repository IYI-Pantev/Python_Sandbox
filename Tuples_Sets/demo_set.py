# a = {1, 2, 3}
# b = {3, 4, 5}
# print(type(a))
# a.add(100)
#
# print(a)
# a.add(1)
# print(a)  # cant duplicate
# c = a.union(b)
# print(c)
#
# d = {1, 2}
# e = {1, 2, 3, 4}
#
# print(e.issuperset(d))
# f = {1, 2, 3, 4}
# g = {3, 4, 5, 6}
#
# h = f.symmetric_difference(g)
# print(h)

a = {1, 2, 3, 4}
b = {1, 2, 100}

print(a.difference(b))  # every element in a that is not present in b
print(a | b)
print(a ^ b)