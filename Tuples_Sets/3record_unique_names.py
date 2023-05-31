# write program, which take a list of names and print only the unique ones
# the output order doesn't matter
number_of_names = int(input())
set_of_names = set()
for _ in range(number_of_names):
    current_name = input()
    set_of_names.add(current_name)

x = list(set_of_names)
[print(i) for i in x]

# input: 8
# Lee
# Joey
# Lee
# Joe
# Alan
# Alan
# Peter
# Joey
