# Given two lists of strings print a new list of the strings
# that contains words from the first list which are substrings
# of any of the strings in the second list (only unique values)
# Input
# There will be 2 lines of input: the two lists separated by "

substrings = input().split(", ")
words = input().split(", ")

occ_substrings = []
for substr in substrings:
    for word in words:
        if substr in word:
            occ_substrings.append(substr)

print(set(occ_substrings))
