text = "Hello there some nums 1234. That is it"

index = 0
num = ""

while index < len(text):
    if text[index].isdigit():
        while text[index].isdigit():
            num += text[index]
            index += 1
        num = int(num)
    index += 1

print(num)

