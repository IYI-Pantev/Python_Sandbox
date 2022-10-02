string = input().split(' ')

data = []

team_A = 11
team_B = 11

for i in string:
    data.append(i)

data.sort()

for card in data:
    if 'A' in card:
        team_A -= 1
    if 'B' in card:
        team_B -= 1
print(f"Team A - {team_A}; Team B - {team_B}")

if team_A < 7 or team_B < 7:
    print("Game was terminated")
