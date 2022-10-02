# Calculate how many courses will be needed to elevate n
# persons by using an elevator with capacity of p persons.
# The input holds two lines: the number of people n
# and the capacity p of the elevator.

import math
persons = int(input("Persons: "))

capacity = int(input("Enter capacity: "))

courses = math.ceil(persons/capacity)

print(f"There will be needed {courses} courses\nto elevate the persons")




