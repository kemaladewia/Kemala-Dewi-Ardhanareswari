class User:
    """A simple attempt to model a user profile."""
   
    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user's profile information."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0
    
    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f" Username: {self.username}")
        print(f" Email: {self.email}")
        print(f" Location: {self.location}")
    
    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")
    
    def increment_login_attempts(self):
        """Increment the value of login_attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the value of login_attempts to 0."""
        self.login_attempts = 0

mala = User('mala', 'dewi', 'k_mala', 'k_mala@example.com', 'alaska')
mala.describe_user()
mala.greet_user()

print("\nMaking 3 login attempts...")
mala.increment_login_attempts()
mala.increment_login_attempts()
mala.increment_login_attempts()
print(f" Login attempts: {mala.login_attempts}")

print("Resetting login attempts...")
mala.reset_login_attempts()
print(f" Login attempts: {mala.login_attempts}")