pets = [
    {'name': 'mochi', 'animal': 'cat', 'owner': 'sari'},
    {'name': 'bruno', 'animal': 'dog', 'owner': 'budi'},
    {'name': 'kiko', 'animal': 'parrot', 'owner': 'rina'},
    {'name': 'snow', 'animal': 'rabbit', 'owner': 'dimas'},
]

for pet in pets:
    print(f"{pet['name'].title()} is a {pet['animal']} "
          f"owned by {pet['owner'].title()}.")