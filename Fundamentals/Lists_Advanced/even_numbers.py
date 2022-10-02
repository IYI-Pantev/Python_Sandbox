# Write a program that reads a single string with numbers
# separated by comma and space ", "
# Print the indices of all even numbers

numbers = list(map(int, input().split(", ")))
even_indices = []

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_indices.append(i)

print(even_indices)
