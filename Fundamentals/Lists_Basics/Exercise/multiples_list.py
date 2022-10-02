# Write a program that receives two numbers (factor and count)
# and creates a list with length of the given count
# and contains only elements that are multiples of the given factor.

factor = int(input('factor:'))
count = int(input('count:'))

given_list = []

for num in range(1, count+1):
    if num % factor == 0:
        given_list.append(num)

print(given_list)



