# record a car number when enters, remove when leaves
# first line N of commands
# in/out, carnum
# print the cars in the parking or Parking Lot is Empty.

parking_lot = set()

n = int(input())

for _ in range(n):
    command = input().split(', ')
    if command[0] == 'IN':
        parking_lot.add((command[1]))
    else:
        parking_lot.remove(command[1])

if len(parking_lot) > 0:
    [print(i) for i in list(parking_lot)]
else:
    print("Parking Lot is Empty.")


# input: 5
# IN, CB8125CA
# IN, CB1046BA
# IN, CB8989BA
# OUT, CB1046BA
# IN, CB6969BA