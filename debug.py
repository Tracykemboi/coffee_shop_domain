# Import necessary classes from their respective modules
from customer import Customer
from coffee import Coffee

# Create some customers and coffees
alice = Customer("Alice")  # Create a Customer object for Alice
bob = Customer("Bob")      # Create a Customer object for Bob
latte = Coffee("Latte")    # Create a Coffee object for Latte
espresso = Coffee("Espresso")  # Create a Coffee object for Espresso

# Create some orders
alice.create_order(latte, 3.5)     # Alice orders a Latte for $3.5
alice.create_order(espresso, 2.5)  # Alice orders an Espresso for $2.5
bob.create_order(latte, 3.0)       # Bob orders a Latte for $3.0

# Test some methods
# Print Alice's orders
print(f"Alice's orders: {alice.orders()}")

# Print the types of coffee Bob has ordered
print(f"Bob's coffees: {bob.coffees()}")

# Print the customers who have ordered a Latte
print(f"Latte's customers: {latte.customers()}")

# Print the average price of Espresso orders
print(f"Espresso's average price: {espresso.average_price()}")

# Find and print the name of the customer who spent the most on Lattes
print(f"Most aficionado of Latte: {Customer.most_aficionado(latte).name}")