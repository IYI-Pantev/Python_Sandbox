
# Two lines of input:
# list of employee's happiness
# happiness improvement factor (single number)
# Multiply the numbers from the list by the factor,
# filter the numbers >= average in the new list and print the result
#

employees_happiness = [int(happiness) for happiness in input().split()]
factor = int(input())
factored_employees_happiness = list(map(lambda h: h * factor, employees_happiness))
average_happiness = sum(factored_employees_happiness) / len(factored_employees_happiness)
happy_employees = [e for e in factored_employees_happiness if e >= average_happiness]
unhappy_employees = [e for e in factored_employees_happiness if e < average_happiness]

print(
    f'Score: {len(happy_employees)}/{len(employees_happiness)}. Employees are{[" not", ""][int(len(happy_employees) >= len(unhappy_employees))]} happy!')