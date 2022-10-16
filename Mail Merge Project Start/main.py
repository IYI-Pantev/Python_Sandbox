#Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as invited:
    names = invited.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    content = letter.read()

for name in names:
    stripped_name = name.strip()
    new_letter = content.replace(PLACEHOLDER, stripped_name)
    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
        completed_letter.write(new_letter)
