n = int(input())
#symbol = input()
total_sum = 0
ascii_symbol = 0
# ascii_symbol = ord(symbol) # dava aski na char
# print(ascii_symbol)

for _ in range(n):
    symbol = input()
    ascii_symbol = ord(symbol)
    total_sum += ascii_symbol

print(total_sum)
