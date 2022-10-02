# Write a program that receives a single string
# containing numbers separated by a single space.
# Print a list containing the opposite of each number.

data = input().split()
inverted = []
for i in data:
    i = int(i)
    inverted.append(i * -1)
print(inverted)