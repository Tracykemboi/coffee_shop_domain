class Coffee:
    def __init__(self, name):
        # Initialize the Coffee object with a name
        self.name = name
        # Initialize an empty list to store orders for this coffee
        self._orders = []

    @property
    def name(self):
        # Getter for the name attribute
        return self._name

    @name.setter
    def name(self, value):
        # Setter for the name attribute
        # Ensure that the value is a string
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        # Ensure that the name is at least 3 characters long
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters long")
        self._name = value

    def orders(self):
        # Return the list of orders for this coffee
        return self._orders

    def customers(self):
        # Return a list of unique customers who have ordered this coffee
        return list(set(order.customer for order in self._orders))

    def num_orders(self):
        # Return the total number of orders for this coffee
        return len(self._orders)

    def average_price(self):
        # Calculate and return the average price of orders for this coffee
        if not self._orders:
            return 0
        # Calculate the total price of all orders
        total_price = sum(order.price for order in self._orders)
        # Return the average price
        return total_price / len(self._orders)