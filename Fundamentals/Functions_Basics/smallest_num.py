def smallest_num(num_list):
    num_list.sort()
    smallest = num_list[0]
    return smallest


data = input("Enter three numbers: ").split(' ')

numbers = [int(x) for x in data]

print(smallest_num(numbers))

# second way
a = int(input())
b = int(input())
c = int(input())


def smallest_num(num1, num2, num3):
    smetka = min(num1, num2, num3)
    return smetka
# print(smallest_num(a,b,c))
