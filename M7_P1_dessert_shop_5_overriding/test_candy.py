import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from candy import Candy



class TestCandy:
    def test_default(self):
        candy = Candy()
        assert candy.name == "BaseCandy"
        assert candy.candy_weight == 0.0
        assert candy.price_per_pound == 0.0

    
    def test_nominal(self):
        candy = Candy("Swedish Fish", 0.5, 2.50)
        assert candy.name == "Swedish Fish"
        assert candy.candy_weight == 0.5
        assert candy.price_per_pound == 2.5

    
    def test_getters(self):
        candy = Candy("Jolly Rancher", 0.2, 1.50)
        assert candy.name == "Jolly Rancher"
        assert candy.candy_weight == 0.2
        assert candy.price_per_pound == 1.50

    
    def test_setters(self):
        candy = Candy()
        
        candy.name = "Kit-Kat"
        assert candy.name == "Kit-Kat"

        candy.candy_weight = 15
        assert candy.candy_weight == 15

        candy.price_per_pound = 4.00
        assert candy.price_per_pound == 4.00

        with pytest.raises(TypeError):
            candy.candy_weight = "invalid weight"

        with pytest.raises(ValueError):
            candy.candy_weight = -1

        with pytest.raises(TypeError):
            candy.price_per_pound = "invalid price"

        with pytest.raises(ValueError):
            candy.price_per_pound = -1


    def test_calculate_cost(self):
        item = Candy(candy_weight=1, price_per_pound=1)
        assert item.calculate_cost() == 1

    
    def test_calculate_tax(self):
        item = Candy(candy_weight=1, price_per_pound=1)
        item.tax_percent = 100
        assert item.calculate_tax() == 1

