cities = {
    'jakarta': {
        'country': 'indonesia',
        'population': 11_000_000,
        'fact': 'It was known as Batavia during the Dutch colonial era.',
    },
    'tokyo': {
        'country': 'japan',
        'population': 14_000_000,
        'fact': 'It was called Edo until 1868.',
    },
    'sydney': {
        'country': 'australia',
        'population': 5_400_000,
        'fact': 'Its Opera House opened in 1973.',
    },
}

for city, info in cities.items():
    print(f"\n{city.title()}")
    print(f"\tCountry: {info['country'].title()}")
    print(f"\tPopulation: about {info['population']:,}")
    print(f"\tFact: {info['fact']}")