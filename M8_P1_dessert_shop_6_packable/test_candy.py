import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from candy import Candy



class TestCandy:
    def test_default(self):
        item = Candy()
        assert item.name == "BaseCandy"
        assert item.candy_weight == 0.0
        assert item.price_per_pound == 0.0

    
    def test_nominal(self):
        item = Candy("Swedish Fish", 0.5, 2.50)
        assert item.name == "Swedish Fish"
        assert item.candy_weight == 0.5
        assert item.price_per_pound == 2.5

    
    def test_getters(self):
        item = Candy("Jolly Rancher", 0.2, 1.50)
        assert item.name == "Jolly Rancher"
        assert item.candy_weight == 0.2
        assert item.price_per_pound == 1.50

    
    def test_setters(self):
        item = Candy()
        
        item.name = "Kit-Kat"
        assert item.name == "Kit-Kat"

        item.candy_weight = 15
        assert item.candy_weight == 15

        item.price_per_pound = 4.00
        assert item.price_per_pound == 4.00

        with pytest.raises(TypeError):
            item.candy_weight = "invalid weight"

        with pytest.raises(ValueError):
            item.candy_weight = -1

        with pytest.raises(TypeError):
            item.price_per_pound = "invalid price"

        with pytest.raises(ValueError):
            item.price_per_pound = -1


    def test_calculate_cost(self):
        item = Candy(candy_weight=1, price_per_pound=1)
        assert item.calculate_cost() == 1

    
    def test_calculate_tax(self):
        item = Candy(candy_weight=1, price_per_pound=1)
        item.tax_percent = 100
        assert item.calculate_tax() == 1


    def test_packaging(self):
        item = Candy()
        assert item.packaging == "Bag"