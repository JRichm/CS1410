import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from order import Order
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
