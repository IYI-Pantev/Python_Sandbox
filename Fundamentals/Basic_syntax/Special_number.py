n = int(input())

for num in range(1, n + 1):
    sum_of_digits = 0
    number = num
    while num > 0:
        digit = num % 10
        sum_of_digits += digit
        num = int(num / 10)
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{number} -> True")
    else:
        print(f"{number} -> False")
