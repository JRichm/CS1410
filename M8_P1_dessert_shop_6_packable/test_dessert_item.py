import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from cookie import Cookie
from dessert_item import DessertItem



class TestDessertItem:
    def test_default(self):
        item = Cookie()
        assert item.name == "BaseCookie"


    def test_nominal(self):
        item = Cookie("Chocolate Cake")
        assert item.name == "Chocolate Cake"

    
    def test_getter(self):
        item = Cookie("Brownie")
        assert item.name == "Brownie"

        item2 = Cookie("Cheesecake")
        name = item2.name
        assert name == "Cheesecake"
        

    def test_setter(self):
        item = Cookie()
        item.name = "Cheesecake"
        assert item.name == "Cheesecake"

        with pytest.raises(TypeError):
            item.name = 123

        with pytest.raises(ValueError):
            item.name = ""

    
    def test_tax_percent(self):
        item = Cookie()
        assert item.tax_percent == 7.25


    def test_set_tax_percent(self):
        item = Cookie()
        item.tax_percent = 6.25
        assert item.tax_percent == 6.25


    def test_get_packaging(self):
        item = Cookie()
        assert item.packaging == "Box"

    
    def test_set_packaging(self):
        item = Cookie()
        item.packaging = "Plate"
        assert item.packaging == "Plate"