import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from dessert_item import DessertItem



class TestDessertItem:
    def test_default(self):
        item = DessertItem()
        assert item.name == ""


    def test_nominal(self):
        item = DessertItem("Chocolate Cake")
        assert item.name == "Chocolate Cake"

    
    def test_getter(self):
        item = DessertItem("Brownie")
        assert item.name == "Brownie"

        item2 = DessertItem("Cheesecake")
        name = item2.name
        assert name == "Cheesecake"
        

    def test_setter(self):
        item = DessertItem()
        item.name = "Cheesecake"
        assert item.name == "Cheesecake"

        with pytest.raises(TypeError):
            item.name = 123

        with pytest.raises(ValueError):
            item.name = ""