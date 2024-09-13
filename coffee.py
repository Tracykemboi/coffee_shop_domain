class Coffee:
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
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters long")
        self._name = value
    def orders(self):
        return self._orders

    def customers(self):
        return list(set(order.customer for order in self._orders))