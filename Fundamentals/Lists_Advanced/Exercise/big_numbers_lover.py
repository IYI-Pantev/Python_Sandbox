# You will receive a single line containing numbers separated by a single space.
# Sort and reverse the numbers then return them as a string.

# numbers = [x for x in input().split()]
numbers = input().split()

# numbers.reverse()
numbers.sort(reverse=True)
# for i in range(len(numbers)):
#     print(numbers[i])

print(*numbers, sep='') # Without using loops: * symbol is use to print the list elements in a single line with space. T
# o print all elements in new lines or separated by space use sep=”\n” or sep=”, ” respectively
