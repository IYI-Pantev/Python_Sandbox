gifts_list = input("Enter gifts: ").split()

command = input()

while command != "No Money":
    command = command.split()
    if command[0] == "OutOfStock":
        for i in range(len(gifts_list)):
            if command[1] == gifts_list[i]:
                gifts_list[i] = "None"
    elif command[0] == "Required":
        index = command[2]
        gifts_list[int(index)] = command[1]
    elif command[0] == "JustInCase":
        gifts_list[-1] = command[1]

    command = input()

final_note = [x for x in gifts_list if x != "None"]
print(*final_note, sep=" ")
