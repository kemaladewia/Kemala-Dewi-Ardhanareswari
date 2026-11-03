favorite_places = {
    'mala': ['malioboro', 'prambanan', 'kaliurang'],
    'lila': ['bromo'],
    'cila': ['ubud', 'uluwatu'],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places:")
    for place in places:
        print(f"= {place.title()}")