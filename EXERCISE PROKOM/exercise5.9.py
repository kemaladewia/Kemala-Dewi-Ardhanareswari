usernames = ['admin', 'mala', 'nabila', 'aira', 'rara']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you to see a status report?")
    else:
        print(f"Hello {username.title()} thank you for logging in again.")
else:
    print("We need to find some users!")

usernames = []
print()

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")