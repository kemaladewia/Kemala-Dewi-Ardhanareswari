def make_shirt(size='large', message='I love Python'):
    """Ringkas ukuran kaos dan tulisan yang dicetak di atasnya."""
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')

make_shirt() 
make_shirt(size='medium') 
make_shirt('small', 'Simple is better than complex.') 