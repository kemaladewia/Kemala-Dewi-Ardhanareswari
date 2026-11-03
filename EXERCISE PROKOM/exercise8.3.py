def make_shirt(size, message):
    """Ringkas ukuran kaos dan tulisan yang dicetak di atasnya."""
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')

# Argumen posisional
make_shirt('medium', 'Hello, World!')

# Argumen keyword
make_shirt(message='Readability counts.', size='small')