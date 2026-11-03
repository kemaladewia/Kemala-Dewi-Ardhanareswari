users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        'field': 'physics',
        'languages': ['german', 'english'],
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        'field': 'chemistry',
        'languages': ['polish', 'french'],
    },
    'bjhabibie': {
        'first': 'b.j.',
        'last': 'habibie',
        'location': 'jakarta',
        'field': 'aerospace engineering',
        'languages': ['indonesian'],
    },
}

for username, user_info in users.items():
    full_name = f"{user_info['first']} {user_info['last']}"
    languages = [language.title() for language in user_info['languages']]
    
    print(f"\nUsername: {username}")
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {user_info['location'].title()}")
    print(f"\tField: {user_info['field'].title()}")
    
    if len(languages) == 1:
        print(f"\tLanguage: {languages[0]}")
    else:
        print(f"\tLanguages: {', '.join(languages)}")

print(f"\nTotal users: {len(users)}")