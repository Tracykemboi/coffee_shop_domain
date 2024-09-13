import pytest
from coffee import Coffee
from customer import Customer

def test_coffee_creation():
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"

def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee("La")  # Too short
    with pytest.raises(ValueError):
        Coffee(123)  # Not a string

def test_orders():
    coffee = Coffee("Cappuccino")
    customer = Customer("Alice")
    order1 = customer.create_order(coffee, 3.5)
    order2 = customer.create_order(coffee, 4.0)
    assert len(coffee.orders()) == 2
    assert order1 in coffee.orders()
    assert order2 in coffee.orders()

def test_customers():
    coffee = Coffee("Espresso")
    customer1 = Customer("Bob")
    customer2 = Customer("Charlie")
    customer1.create_order(coffee, 2.5)
    customer2.create_order(coffee, 2.7)
    customers = coffee.customers()
    assert len(customers) == 2
    assert customer1 in customers
    assert customer2 in customers

def test_num_orders():
    coffee = Coffee("Mocha")
    customer = Customer("David")
    customer.create_order(coffee, 4.0)
    customer.create_order(coffee, 4.2)
    assert coffee.num_orders() == 2

def test_average_price():
    coffee = Coffee("Americano")
    customer = Customer("Eve")
    customer.create_order(coffee, 3.0)
    customer.create_order(coffee, 3.5)
    assert coffee.average_price() == 3.25

def test_average_price_no_orders():
    coffee = Coffee("Macchiato")
    assert coffee.average_price() == 0