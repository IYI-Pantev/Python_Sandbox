import re

# pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
#
# text = input().split(", ")
#
# valid_names = []
# for name in text:
#     if re.match(pattern, name):
#         valid_names.append(name)
#
# print("\n".join(valid_names))

# second way
names = input()

regex = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

matches = re.findall(regex, names) #Returns a list containing all matches

print("\n".join(matches))