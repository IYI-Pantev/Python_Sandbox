import re

text_line = input()

regex = r"\d+"
all_numbers = []

while not text_line == "":
    numbers = re.findall(regex, text_line)
    all_numbers.extend(numbers)

    text_line = input()

print(*all_numbers)