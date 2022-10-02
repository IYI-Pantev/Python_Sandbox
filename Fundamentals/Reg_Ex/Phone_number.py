import re
text = input()

pattern = r"\+359( |-)2\1\d{3}\1\d{4}\b"

# matches = re.findall(pattern, text)
# print(matches) # returns mathces of the group ()!!!

#1st way
# matches = re.finditer(pattern, text)
# for match in matches:
#     print(match.group())

#second way
valid_numbers = [obj.group() for obj in re.finditer(pattern, text)]

print(", ".join(valid_numbers))

