import pytest
from customer import Customer
from coffee import Coffee

def test_customer_creation():
    customer = Customer("Alice")
    assert customer.name == "Alice"

def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer("")  # Too short
    with pytest.raises(ValueError):
        Customer("ThisNameIsTooLong")  # Too long

def test_create_order():
    customer = Customer("Bob")
    coffee = Coffee("Latte")
    order = customer.create_order(coffee, 3.5)
    assert order in customer.orders()
    assert coffee in customer.coffees()

def test_coffees():
    customer = Customer("Charlie")
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")
    customer.create_order(latte, 3.5)
    customer.create_order(espresso, 2.5)
    customer.create_order(latte, 4.0)
    assert set(customer.coffees()) == {latte, espresso}

def test_most_aficionado():
    alice = Customer("Alice")
    bob = Customer("Bob")
    latte = Coffee("Latte")
    alice.create_order(latte, 4.0)
    alice.create_order(latte, 4.5)
    bob.create_order(latte, 3.5)
    assert Customer.most_aficionado(latte) == alice

def test_most_aficionado_no_orders():
    coffee = Coffee("Espresso")
    assert Customer.most_aficionado(coffee) is None