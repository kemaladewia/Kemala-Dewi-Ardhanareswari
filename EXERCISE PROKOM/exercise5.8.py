usernames = ['admin', 'mala', 'nabila', 'aira', 'rara']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you to see a status report?")
    else:
        print(f"Hello {username.title()} thank you for logging in again.")