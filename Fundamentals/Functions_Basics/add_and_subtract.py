a = int(input())
b = int(input())
c = int(input())


def sum_numbers(num1, num2):
    return num1 + num2


sum_of_two = sum_numbers(a, b)


def subtract(x, y):
    return x - y


final = subtract(sum_of_two, c)

print(final)