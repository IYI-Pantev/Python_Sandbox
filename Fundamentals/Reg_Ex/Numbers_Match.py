import re

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

text = input()

matches = re.finditer(pattern, text)
print(matches)

for match in matches:
    print(match)

for match in matches:
    print(match.group(), end=" ")