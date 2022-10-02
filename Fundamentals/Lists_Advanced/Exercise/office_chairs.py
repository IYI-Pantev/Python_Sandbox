n_rooms = int(input())
free_chairs = 0
are_chairs_enough = True
for room_num in range(1, n_rooms + 1):
    chairs, n_people = input().split()
    n_people = int(n_people)
    difference = abs(len(chairs) - n_people)
    if len(chairs) < n_people:
        print(f"{difference} more chairs needed in room {room_num}")
        are_chairs_enough = False
    else:
        free_chairs += difference


if are_chairs_enough:
    print(f"Game on {free_chairs} free chairs left")