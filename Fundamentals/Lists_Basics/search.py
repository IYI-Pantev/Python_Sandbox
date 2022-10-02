n = int(input("Enter number of activities: "))
hustles = []
searched_word = input("Enter the searched word: ")

for i in range(n):
    word = input()
    hustles.append(word)
print(hustles)

for x in range(len(hustles)-1, -1, -1):
    current = hustles[x]
    if searched_word not in current:
        hustles.remove(current)


print(hustles)