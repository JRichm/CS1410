from customer import Customer
from order import Order
from cookie import Cookie

class TestDessertItem:
    def setup_method(self):
        Customer._next_id = 1000


    def test_defualt(self):
        customer = Customer()
        assert customer.customer_id == 1000
        assert customer.customer_name == "BaseCustomer"
        assert customer.order_history == []


    def test_nominal(self):
        customer = Customer("James")
        assert customer.customer_name == "James"


    def test_get_id(self):
        customer = Customer()
        assert customer.customer_id == 1000


    def test_get_name(self):
        customer = Customer()
        assert customer.customer_name == "BaseCustomer"


    def test_name_setter(self):
        customer = Customer()
        customer.customer_name = "James"
        assert customer.customer_name == "James"

    
    def test_add_order(self):
        item = Cookie()

        order = Order()
        order.add(item)

        customer = Customer()
        customer.add2history(order)

        assert customer.order_history == [order]


    def test_next_id(self):
        customer_1 = Customer()
        customer_2 = Customer()

        assert customer_1.customer_id == 1000
        assert customer_2.customer_id == 1001

