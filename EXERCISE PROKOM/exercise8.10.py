def show_messages(messages):
    """Cetak setiap pesan di dalam list."""
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Cetak tiap pesan, lalu pindahkan ke sent_messages."""
    print("Sending all messages:")
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)

messages = [
    "See you at 7!",
    "Running late, sorry.",
    "Don't forget the slides.",
]
sent_messages = []

send_messages(messages, sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)