from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charizard"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"


print(table)

