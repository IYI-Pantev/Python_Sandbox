def odd_even_sum(n):
    even_sum = 0
    odd_sum = 0
    current_num = 0
    while n > 0:
        current_num = n % 10
        if current_num % 2 == 0:
            even_sum += 1
        elif current_num % 2 != 0:
            odd_sum += 1
        n = int(n / 10)
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = int(input("Enter a number: "))

print(odd_even_sum(number))

# second way
#single_num = input()
# def number(a):
#     odd_sum = 0
#     even_sum = 0
#     for i in single_num:
#         i = int(i)
#         if i % 2 == 0:
#             even_sum += i
#         else:
#             odd_sum += i
#     print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')
# number(single_num)