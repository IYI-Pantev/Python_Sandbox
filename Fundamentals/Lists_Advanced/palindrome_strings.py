# Write a program that receives on the first line words separated
# by a space and a searched palindrome on the second
# Print all the palindromes on the first line
# Print all the occurrences of the searched palindrome in the format:
# "Found palindrome {count} times"
#

strings = input().split(" ")
searched_palindrome = input()
palindromes = []
for word in strings:
    if word == "".join(reversed(word)):
        palindromes.append(word)
print(f"{palindromes}")
print(f"Found palindrome {palindromes.count(searched_palindrome)} times")
