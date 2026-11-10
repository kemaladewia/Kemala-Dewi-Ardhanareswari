class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print a summary of the restaurant."""
        name = self.restaurant_name.title()
        print(f"{name} serves wonderful {self.cuisine_type}.")
    
    def open_restaurant(self):
        """Print a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name.title()} is now open. Come on in!")

    def set_number_served(self, number_served):
        """Set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Add the given number of customers to the number served."""
        self.number_served += additional_served

class IceCreamStand(Restaurant):
    """Represent aspects of a restaurant, specific to ice cream stands."""

    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an ice cream stand.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display the flavors available."""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

big_one = IceCreamStand('the big one')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry', 'durian']

big_one.describe_restaurant()
big_one.show_flavors()