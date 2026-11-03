favorite_numbers = {
    'mala': [7, 14],
    'lila': [3],
    'cila': [21, 8, 1],
    'ala': [10, 100],
    'ama': [42],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"- {number}")