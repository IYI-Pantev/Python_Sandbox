data = input().split()

stock = {}
for i in range(0, len(data), 2):
    current_product = data[i]
    quantity = int(data[i + 1])
    stock[current_product] = int(quantity)


search = input().split()

for product in search:
    if product in stock:
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")