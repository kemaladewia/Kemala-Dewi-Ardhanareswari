rivers = {
    'nile' : 'egypt',
    'amazon' : 'america',
    'kapuas' : 'indonesia',
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nRivers in this dictionary:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nCountries in this dictionary:")
for country in rivers.values():
    print(f"- {country.title()}")