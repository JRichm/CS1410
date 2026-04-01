import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from order import Order
from candy import Candy
from cookie import Cookie
from icecream import IceCream
from sundae import Sundae
from payable import PayType


class TestOrder:
    def test_default_payment_method(self):
        order = Order()
        assert order.payment_method == PayType.CASH


    def test_payment_method_getter(self):
        order = Order()
        order._payment_method = PayType.CARD
        assert order.payment_method == PayType.CARD


    def test_payment_method_setter_cash(self):
        order = Order()
        order.payment_method = PayType.CASH
        assert order.payment_method == PayType.CASH


    def test_payment_method_setter_card(self):
        order = Order()
        order.payment_method = PayType.CARD
        assert order.payment_method == PayType.CARD


    def test_payment_method_setter_phone(self):
        order = Order()
        order.payment_method = PayType.PHONE
        assert order.payment_method == PayType.PHONE


    def test_set_invalid_payment_method(self):
        order = Order()
        with pytest.raises(TypeError):
            order.payment_method = "bitcoin"    


    def test_sort(self):
        order = Order()
        order.add(Candy('Candy Corn', 1.5, 0.25))
        order.add(Candy('Gummy Bears', 0.25, 0.35))
        order.add(Cookie('Chocolate Chip', 6, 3.99))
        order.add(IceCream('Pistachio', 2, 0.79))
        order.add(Sundae('Vanilla', 3, 0.69, 'Hot Fudge', 1.29))
        order.add(Cookie('Oatmeal Raisin', 2, 3.45))

        order.sort()

        prices = [item.calculate_cost() for item in order.order]

        assert prices == sorted(prices)


