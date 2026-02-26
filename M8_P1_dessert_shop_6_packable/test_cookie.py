import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from cookie import Cookie



class TestCookie:
    def test_default(self):
        item = Cookie()
        assert item.name == "BaseCookie"
        assert item.cookie_quantity == 0
        assert item.price_per_dozen == 0.0

    
    def test_nominal(self):
        item = Cookie("Chocolate Chip", 12, 16)
        assert item.name == "Chocolate Chip"
        assert item.cookie_quantity == 12
        assert item.price_per_dozen == 16


    def test_getters(self):
        item = Cookie("Peanut Butter", 6, 18)
        assert item.name == "Peanut Butter"
        assert item.cookie_quantity == 6
        assert item.price_per_dozen == 18


    def test_setters(self):
        item = Cookie()

        item.name = "Sugar Cookie"
        assert item.name == "Sugar Cookie"

        item.cookie_quantity = 12
        assert item.cookie_quantity == 12

        item.price_per_dozen = 15.00
        assert item.price_per_dozen == 15.00

        with pytest.raises(TypeError):
            item.cookie_quantity = "invalid cookie_quantity"

        with pytest.raises(ValueError):
            item.cookie_quantity = -1

        with pytest.raises(TypeError):
            item.price_per_dozen = "invalid price_per_dozen"

        with pytest.raises(ValueError):
            item.price_per_dozen = -1


    def test_calculate_cost(self):
        item = Cookie(cookie_quantity=12, price_per_dozen=1)
        assert item.calculate_cost() == 1

    
    def test_calculate_tax(self):
        item = Cookie(cookie_quantity=12, price_per_dozen=1)
        item.tax_percent = 100
        assert item.calculate_tax() == 1


    def test_packaging(self):
        item = Cookie()
        assert item.packaging == "Box"