""""A simple attempt to model a restaurant."""

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print a summary of the restaurant."""
        name = self.restaurant_name.title()
        print(f"{name} serves wonderful {self.cuisine_type}.")

    def open_restaurant(self):
        """Print a message indicating that the restaurant is open."""   
        print(f"{self.restaurant_name.title()} is now open. Come on in!")

restaurant = Restaurant('warung soto pak seto', 'indonesia food')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()