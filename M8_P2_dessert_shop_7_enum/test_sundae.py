import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from sundae import Sundae


class TestSundae:
    def test_default(self):
        sundae = Sundae()
        assert sundae.name == "BaseSundae"
        assert sundae.scoop_count == 0
        assert sundae.price_per_scoop == 0.0
        assert sundae.topping_name == ""
        assert sundae.topping_price == 0.0

    
    def test_nominal(self):
        sundae = Sundae("Hot Fudge", 3, 5.00, "Fudge", 2.00)
        assert sundae.name == "Hot Fudge"
        assert sundae.scoop_count == 3
        assert sundae.price_per_scoop == 5.00
        assert sundae.topping_name == "Fudge"
        assert sundae.topping_price == 2.00


    def test_getters(self):
        sundae = Sundae("Banana Split", 3, 3.00, "Banana", 1.00)
        assert sundae.name == "Banana Split"
        assert sundae.scoop_count == 3
        assert sundae.price_per_scoop == 3.00
        assert sundae.topping_name == "Banana"
        assert sundae.topping_price == 1.00


    def test_setters(self):
        sundae = Sundae()

        sundae.name = "Tripple Gooberberry Sunrise"
        assert sundae.name == "Tripple Gooberberry Sunrise"

        sundae.scoop_count = 5
        assert sundae.scoop_count == 5

        sundae.price_per_scoop = 6.00
        assert sundae.price_per_scoop == 6.00

        sundae.topping_name = "Chocolate Sauce"
        assert sundae.topping_name == "Chocolate Sauce"

        sundae.topping_name = "Banana"
        assert sundae.topping_name == "Banana"

        sundae.topping_name = "Maraschino Cherries"
        assert sundae.topping_name == "Maraschino Cherries"

        sundae.topping_name = "M&M's"
        assert sundae.topping_name == "M&M's"

        sundae.topping_name = "Maraschino Cherries"
        assert sundae.topping_name == "Maraschino Cherries"

        sundae.topping_name = "Licorice"
        assert sundae.topping_name == "Licorice"

        with pytest.raises(TypeError):
            sundae.scoop_count = "invalid scoop_count"

        with pytest.raises(ValueError):
            sundae.scoop_count = -1

        with pytest.raises(TypeError):
            sundae.price_per_scoop = "invalid price_per_scoop"

        with pytest.raises(ValueError):
            sundae.price_per_scoop = -1

        with pytest.raises(TypeError):
            sundae.topping_name = 1

        with pytest.raises(ValueError):
            sundae.topping_name = ""

        with pytest.raises(TypeError):
            sundae.topping_price = "invalid topping_price"

        with pytest.raises(ValueError):
            sundae.topping_price = -1


    def test_calculate_cost(self):
        item = Sundae(scoop_count=1, price_per_scoop=1, topping_price=1)
        assert item.calculate_cost() == 2

    
    def test_calculate_tax(self):
        item = Sundae(scoop_count=1, price_per_scoop=1, topping_price=1)
        item.tax_percent = 50
        assert item.calculate_tax() == 1


    def test_packaging(self):
        item = Sundae()
        assert item.packaging == "Boat"