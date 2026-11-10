from random import randint

class Die:
    """Represent a die, which can be rolled."""

    def __init__(self, sides=6):
        """Initialize the die."""
        self.sides = sides
    
    def roll_die(self):
        """Print a random number between 1 and the number of sides."""
        print(randint(1, self.sides), end=' ')

# Make a 6-sided die, and show the results of 10 rolls.
d6 = Die()
print("10 rolls of a 6-sided die:")
for roll_num in range(10):
    d6.roll_die()

# Make a 10-sided die, and show the results of 10 rolls.
d10 = Die(sides=10)
print("\n\n10 rolls of a 10-sided die:")
for roll_num in range(10):
    d10.roll_die()

# Make a 20-sided die, and show the results of 10 rolls.
d20 = Die(sides=20)
print("\n\n10 rolls of a 20-sided die:")
for roll_num in range(10):
    d20.roll_die()

print()