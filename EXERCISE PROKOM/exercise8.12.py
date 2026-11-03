def make_sandwich(*items):
    """Cetak ringkasan sandwich yang dipesan."""
    print("\nI'll make you a great sandwich:")
    for item in items:
        print(f" ...adding {item} to your sandwich.")
    print("Your sandwich is ready!")

make_sandwich('roast beef')
make_sandwich('turkey', 'lettuce', 'tomato')
make_sandwich('ham', 'cheese', 'pickles', 'mustard', 'onions')