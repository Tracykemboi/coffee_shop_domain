from customer import Customer
from coffee import Coffee

# Create some customers and coffees
alice = Customer("Alice")
bob = Customer("Bob")
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Create some orders
alice.create_order(latte, 3.5)
alice.create_order(espresso, 2.5)
bob.create_order(latte, 3.0)

# Test some methods
print(f"Alice's orders: {alice.orders()}")
print(f"Bob's coffees: {bob.coffees()}")
print(f"Latte's customers: {latte.customers()}")
print(f"Espresso's average price: {espresso.average_price()}")
print(f"Most aficionado of Latte: {Customer.most_aficionado(latte).name}")