import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from ice_cream import IceCream



class TestIceCream:
    def test_default(self):
        icecream = IceCream()
        assert icecream.name == "BaseIceCream"
        assert icecream.scoop_count == 0
        assert icecream.price_per_scoop == 0.0

    
    def test_nominal(self):
        icecream = IceCream("Vanilla", 2, 2.00)
        assert icecream.name == "Vanilla"
        assert icecream.scoop_count == 2
        assert icecream.price_per_scoop == 2.00


    def test_getters(self):
        icecream = IceCream("Chocolate", 3, 2.00)
        assert icecream.name == "Chocolate"
        assert icecream.scoop_count == 3
        assert icecream.price_per_scoop == 2.00


    def test_setters(self):
        icecream = IceCream()

        icecream.name = "Cookies and Cream"
        assert icecream.name == "Cookies and Cream"

        icecream.scoop_count = 2
        assert icecream.scoop_count == 2

        icecream.price_per_scoop = 2.00
        assert icecream.price_per_scoop == 2.00
    
        with pytest.raises(TypeError):
            icecream.scoop_count = "invalid scoop_count"

        with pytest.raises(ValueError):
            icecream.scoop_count = -1

        with pytest.raises(TypeError):
            icecream.price_per_scoop = "invalid price_per_scoop"

        with pytest.raises(ValueError):
            icecream.price_per_scoop = -1


    def test_calculate_cost(self):
        cookie = IceCream(scoop_count=1, price_per_scoop=1)
        assert cookie.calculate_cost() == 1

    
    def test_calculate_tax(self):
        cookie = IceCream(scoop_count=1, price_per_scoop=1)
        cookie.tax_percent = 100
        assert cookie.calculate_tax() == 1

