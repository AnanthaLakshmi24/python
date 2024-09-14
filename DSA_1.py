class Flower:
    def __init__(self, name: str, petals: int, price: float):

        """
        Constructor to initialize the flower's name, number of petals, and price.
        """
        self.name = name
        self.petals = petals
        self.price = price

    def set_name(self, name: str):
        """
        Method to set the flower's name.
        """
        self.name = name
    def get_name(self):
        """
        Method to retrieve the flower's name.
        """
        return self.name

    def set_petals(self, petals: int):
        """
        Method to set the number of petals.
        """
        self.petals = petals

    def get_petals(self):
        """
        Method to retrieve the number of petals.
        """
        return self.petals

    def set_price(self, price: float):
        """
        Method to set the flower's price.
        """
        self.price = price

    def get_price(self):
        """
        Method to retrieve the flower's price.
        """
        return self.price

# Example usage
flower = Flower("Rose", 32, 1.99)
print(f"Name: {flower.get_name()}")
print(f"Petals: {flower.get_petals()}")
print(f"Price: {flower.get_price()}")

flower.set_name("Tulip")
flower.set_petals(6)
flower.set_price(0.99)

print(f"Updated Name: {flower.get_name()}")
print(f"Updated Petals: {flower.get_petals()}")
print(f"Updated Price: {flower.get_price()}")


