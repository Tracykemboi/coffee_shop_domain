import pytest
from order import Order
from customer import Customer
from coffee import Coffee

def test_order_creation():
    customer = Customer("Frank")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 3.5)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 3.5

def test_order_price_validation():
    customer = Customer("Grace")
    coffee = Coffee("Cappuccino")
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)  # Too low
    with pytest.raises(ValueError):
        Order(customer, coffee, 11.0)  # Too high
    with pytest.raises(ValueError):
        Order(customer, coffee, "not a number")  # Not a number

def test_order_customer_validation():
    coffee = Coffee("Espresso")
    with pytest.raises(ValueError):
        Order("not a customer object", coffee, 2.5)

def test_order_coffee_validation():
    customer = Customer("Henry")
    with pytest.raises(ValueError):
        Order(customer, "not a coffee object", 2.5)

def test_order_in_customer_and_coffee():
    customer = Customer("Ivy")
    coffee = Coffee("Mocha")
    order = Order(customer, coffee, 4.0)
    assert order in customer.orders()
    assert order in coffee.orders()