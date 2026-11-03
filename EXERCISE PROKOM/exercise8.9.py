def show_messages(messages):
    """Cetak setiap pesan di dalam list."""
    for message in messages:
        print(message)

messages = [
    "See you at 7!",
    "Running late, sorry.",
    "Don't forget the slides.",
]
show_messages(messages)