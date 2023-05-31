# you will be given numbers. Write program which prints the number
# of occurrences of each number

numbers = [float(i) for i in input().split(" ")]

numbers = tuple(numbers)

result = {}

for num in numbers:
    if num not in result:
        result[num] = 0
    result[num] += 1

for key,value in result.items():
    print(f"{key} - {value} times")

# input: -2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3