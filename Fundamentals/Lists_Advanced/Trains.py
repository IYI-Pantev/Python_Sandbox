#
# You will receive how many wagons the train has.
# Create a list with that length with all zeros.
# Until you receive the command "End", you get some of the following commands:
# •	add {people} -> adds the people in the last wagon
# •	insert {index} {people} -> adds the people at the given wagon
# •	leave {index} {people} -> removes the people from the wagon
# After you receive the "End" command print the train

wagons_n = int(input())
train = [0] * wagons_n

while True:
    command = input()
    if command == 'End':
        break

    tokens = command.split()
    instruction = tokens[0]

    if instruction == 'add':
        count = int(tokens[1])
        train[-1] += count
    elif instruction == 'insert':
        count = int(tokens[2])
        index = int(tokens[1])
        train[index] += count
    elif instruction == 'leave':
        index = int(tokens[1])
        count = int(tokens[2])
        train[index] -= count
print(train)

