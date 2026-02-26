import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from ice_cream import IceCream



class TestIceCream:
    def test_default(self):
        item = IceCream()
        assert item.name == "BaseIceCream"
        assert item.scoop_count == 0
        assert item.price_per_scoop == 0.0

    
    def test_nominal(self):
        item = IceCream("Vanilla", 2, 2.00)
        assert item.name == "Vanilla"
        assert item.scoop_count == 2
        assert item.price_per_scoop == 2.00


    def test_getters(self):
        item = IceCream("Chocolate", 3, 2.00)
        assert item.name == "Chocolate"
        assert item.scoop_count == 3
        assert item.price_per_scoop == 2.00


    def test_setters(self):
        item = IceCream()

        item.name = "Cookies and Cream"
        assert item.name == "Cookies and Cream"

        item.scoop_count = 2
        assert item.scoop_count == 2

        item.price_per_scoop = 2.00
        assert item.price_per_scoop == 2.00
    
        with pytest.raises(TypeError):
            item.scoop_count = "invalid scoop_count"

        with pytest.raises(ValueError):
            item.scoop_count = -1

        with pytest.raises(TypeError):
            item.price_per_scoop = "invalid price_per_scoop"

        with pytest.raises(ValueError):
            item.price_per_scoop = -1


    def test_calculate_cost(self):
        item = IceCream(scoop_count=1, price_per_scoop=1)
        assert item.calculate_cost() == 1

    
    def test_calculate_tax(self):
        item = IceCream(scoop_count=1, price_per_scoop=1)
        item.tax_percent = 100
        assert item.calculate_tax() == 1


    def test_packaging(self):
        item = IceCream()
        assert item.packaging == "Bowl"