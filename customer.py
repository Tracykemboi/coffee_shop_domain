class Customer:
    def __init__(self, name):
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) < 1 or len(value) > 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value
    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))
    