class User:
    """A simple attempt to model a user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user's profile information."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"   Username: {self.username}")
        print(f"   Email: {self.email}")
        print(f"   Location: {self.location}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")

mala = User('mala', 'dewi', 'k_mala', 'k_mala@example.com', 'solo')
mala.describe_user()
mala.greet_user()

lila = User('lila', 'dewi', 'k_lila', 'k_lila@example.com', 'jakarta')
lila.describe_user()
lila.greet_user()

cila = User('cila', 'dewi', 'k_cila', 'k_cila@example.com', 'semarang')
cila.describe_user()
cila.greet_user()