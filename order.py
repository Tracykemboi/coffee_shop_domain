class Order:
    def __init__(self, customer, coffee, price):
        # Initialize the Order object with customer, coffee, and price
        self.customer = customer
        self.coffee = coffee
        self.price = price
        # Add this order to the customer's and coffee's order lists
        customer._orders.append(self)
        coffee._orders.append(self)

    @property
    def customer(self):
        # Getter for the customer attribute
        return self._customer

    @customer.setter
    def customer(self, value):
        # Setter for the customer attribute
        from customer import Customer
        # Ensure that the value is an instance of Customer
        if not isinstance(value, Customer):
            raise ValueError("Customer must be a Customer instance")
        self._customer = value

    @property
    def coffee(self):
        # Getter for the coffee attribute
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        # Setter for the coffee attribute
        from coffee import Coffee
        # Ensure that the value is an instance of Coffee
        if not isinstance(value, Coffee):
            raise ValueError("Coffee must be a Coffee instance")
        self._coffee = value

    @property
    def price(self):
        # Getter for the price attribute
        return self._price

    @price.setter
    def price(self, value):
        # Setter for the price attribute
        # Ensure that the value is a number (int or float)
        if not isinstance(value, (int, float)):
            raise ValueError("Price must be a number")
        # Ensure that the price is within the valid range
        if value < 1.0 or value > 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        self._price = value