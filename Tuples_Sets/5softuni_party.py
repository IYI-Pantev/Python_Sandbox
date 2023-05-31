# check if guest in VIP or Regular list
# reserve codes are 8 characters vip starts with number
# n - number of g. until - END
# print number of guests who did not come and their reserve numbers
# THE VIP must be first
# vip and guests must be sorted in ascending order

n = int(input())
all_guests = set()

for _ in range(n):
    all_guests.add(input())

ticket = input()
arrived = set()
while not ticket == "END":
    arrived.add(ticket)
    ticket = input()

print(len(all_guests - arrived))
list_not_arrived = list(all_guests.difference(arrived))

for guest in sorted(list_not_arrived):
    if guest[0].isdigit():
        print(guest)

for guest in sorted(list_not_arrived):
    if guest[0].isalpha():
        print(guest)


# input: 5
# 7IK9Yo0h
# 9NoBUajQ
# Ce8vwPme
# SVQXQCbc
# tSzE5t0p
# 9NoBUajQ
# Ce8vwPme
# SVQXQCbc
# END