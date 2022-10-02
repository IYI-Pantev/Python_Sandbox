# #For each word:
# •	the second and the last letter are switched (e.g. Hello becomes Holle)
# •	the first letter is replaced by its character code (e.g. H becomes 72)

# cipher = input('Enter cipher: ').split()
#
# for i in range(0, len(cipher)):
#     second_letter = cipher[i][1]
#     cipher[i][1] = cipher[i][-1]
#

message_list = input('Enter message list: ').split()

for word in message_list:
    number = ''
    for char in word:
        if char.isdigit():
            number += char
    first_letter = chr(int(number))
    current_word = first_letter + word[len(number):]
    current_word = list(current_word)
    current_word[1], current_word[-1] = current_word[-1], current_word[1]
    print(f"{''.join(current_word)} ", end="")
