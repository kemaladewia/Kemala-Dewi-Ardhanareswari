current_users = ['Mala', 'LILA', 'ulfi', 'nabila', 'rara']
new_users = ['mala', 'lila', 'Puyes', 'aira', 'salsa']

current_users_lower = [user.lower () for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username '{new_user}' is taken."
              "Please enter a new username.")
    else:
        print(f"The username '{new_user}' is available.")
