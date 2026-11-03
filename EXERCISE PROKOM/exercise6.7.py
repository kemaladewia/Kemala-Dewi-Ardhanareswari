person_1 = {
    'first_name': 'Keylila',
    'last_name': 'Indreswari',
    'age': '18',
    'city': 'Solo',
}

person_2 = {
    'first_name': 'Kemala',
    'last_name': 'Ardhanareswari',
    'age': '18',
    'city': 'Solo',
}

person_3 = {
    'first_name': 'Nabila',
    'last_name': 'Maratu',
    'age': '18',
    'city': 'Ungaran',
}

people = [person_1, person_2, person_3]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"{full_name.title()}, {person['age']}, "
          f"lives in {person['city'].title()}.")