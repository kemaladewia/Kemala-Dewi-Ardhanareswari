class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def  describe_restaurant(self):
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

restaurant = Restaurant('warung sate pak budi', 'indonesian food')
restaurant.describe_restaurant()

print(f"\nNumber served: {restaurant.number_served}")

restaurant.number_served = 430
print(f"Number served: {restaurant.number_served}")

restaurant.set_number_served(1257)
print(f"Number served: {restaurant.number_served}")

restaurant.increment_number_served(239)
print(f"Number served: {restaurant.number_served}")
