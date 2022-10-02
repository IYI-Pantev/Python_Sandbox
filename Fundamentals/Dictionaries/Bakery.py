bakery = {}

data = input().split()

for i in range(0, len(data), 2):
    current_product = data[i]
    quantity = data[i + 1]
    bakery[current_product] = int(quantity)

print(bakery)