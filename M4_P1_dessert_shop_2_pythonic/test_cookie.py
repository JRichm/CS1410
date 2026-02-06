import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from cookie import Cookie



class TestCookie:
    def test_default(self):
        cookie = Cookie()
        assert cookie.name == "BaseCookie"
        assert cookie.cookie_quantity == 0
        assert cookie.price_per_dozen == 0.0

    
    def test_nominal(self):
        cookie = Cookie("Chocolate Chip", 12, 16)
        assert cookie.name == "Chocolate Chip"
        assert cookie.cookie_quantity == 12
        assert cookie.price_per_dozen == 16


    def test_getters(self):
        cookie = Cookie("Peanut Butter", 6, 18)
        assert cookie.name == "Peanut Butter"
        assert cookie.cookie_quantity == 6
        assert cookie.price_per_dozen == 18


    def test_setters(self):
        cookie = Cookie()

        cookie.name = "Sugar Cookie"
        assert cookie.name == "Sugar Cookie"

        cookie.cookie_quantity = 12
        assert cookie.cookie_quantity == 12

        cookie.price_per_dozen = 15.00
        assert cookie.price_per_dozen == 15.00

        with pytest.raises(TypeError):
            cookie.cookie_quantity = "invalid cookie_quantity"

        with pytest.raises(ValueError):
            cookie.cookie_quantity = -1

        with pytest.raises(TypeError):
            cookie.price_per_dozen = "invalid price_per_dozen"

        with pytest.raises(ValueError):
            cookie.price_per_dozen = -1
