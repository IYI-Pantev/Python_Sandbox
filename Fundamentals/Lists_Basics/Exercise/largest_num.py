numbers = input("Enter numbers: ").split(' ')
print(numbers)
numbers = [int(num) for num in numbers]
numbers.sort()
print(numbers)

print(f"The biggest number is {numbers[-1]}")