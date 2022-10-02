#You will receive a todo-notes until you get the command "End".
# The notes will be in the format: "{importance}-{value}".
# Return the list of todo-notes sorted by importance.
# The maximum importance will be 10

command = input()

notes = [0] * 10

while command != 'End':
    tokens = command.split("-")
    priority = int(tokens[0])
    note = tokens[1]
    notes.insert(priority, note)
    command = input()

print(notes)
result = [x for x in notes if x != 0]

print(result)