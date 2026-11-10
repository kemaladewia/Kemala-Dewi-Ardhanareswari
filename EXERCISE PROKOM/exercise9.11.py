from user import Admin
mala = Admin('mala', 'dewi', 'k_mala', 'k_mala@example.com', 'solo')
mala.describe_user()

mala_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
mala.privileges.privileges = mala_privileges

print(f"\nThe admin {mala.username} has these privileges: ")
mala.privileges.show_privileges()