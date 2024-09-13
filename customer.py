class Customer:
    def __init__(self, name):
        # Initialize the Customer object with a name
        self.name = name
        # Initialize an empty list to store the customer's orders
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
        # Ensure that the name length is between 1 and 15 characters
        if len(value) < 1 or len(value) > 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        # Return the list of orders for this customer
        return self._orders

    def coffees(self):
        # Return a list of unique coffees ordered by this customer
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        # Create a new Order instance for this customer
        from order import Order
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        # Find the customer who has spent the most on a specific coffee
        # If no orders for the coffee, return None
        if not coffee._orders:
            return None
        # Create a dictionary to track spending per customer
        customer_spending = {}
        for order in coffee._orders:
            customer_spending[order.customer] = customer_spending.get(order.customer, 0) + order.price
        # Return the customer who spent the most
        return max(customer_spending, key=customer_spending.get)