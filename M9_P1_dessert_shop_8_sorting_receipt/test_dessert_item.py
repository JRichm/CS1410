import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from cookie import Cookie
from candy import Candy
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


    def test_eq_true(self):
        item_1 = Cookie('Chocolate Chip', 12, 1)
        item_2 = Candy('Gummy Bears', 1, 1)
        assert item_1 == item_2


    def test_eq_false(self):
        item_1 = Cookie('Chocolate Chip', 12, 1)
        item_2 = "Gummy Bears"
        assert not item_1 == item_2


    def test_ne_true(self):
        item_1 = Cookie('Chocolate Chip', 12, 1)
        item_2 = Candy('Gummy Bears', 1, 2)
        assert item_1 != item_2


    def test_ne_false(self):
        item_1 = Cookie('Chocolate Chip', 12, 1)
        item_2 = Candy('Gummy Bears', 1, 1)
        assert not item_1 != item_2


    def test_lt_true(self):
        item_1 = Cookie('Chocolate Chip', 12, 1)
        item_2 = Candy('Gummy Bears', 1, 2)
        assert item_1 < item_2


    def test_lt_false(self):
        item_1 = Cookie('Chocolate Chip', 12, 2)
        item_2 = Candy('Gummy Bears', 1, 1)
        assert not item_1 < item_2


    def test_lt_type_error(self):
        item_1 = Cookie('Chocolate Chip', 12, 2)
        item_2 = "Gummy Bears"
        with pytest.raises(TypeError):
            item_1 < item_2


    def test_gt_true(self):
        item_1 = Cookie('Chocolate Chip', 12, 2)
        item_2 = Candy('Gummy Bears', 1, 1)
        assert item_1 > item_2


    def test_gt_false(self):
        item_1 = Cookie('Chocolate Chip', 12, 1)
        item_2 = Candy('Gummy Bears', 1, 2)
        assert not item_1 > item_2


    def test_gt_type_error(self):
        item_1 = Cookie('Chocolate Chip', 12, 1)
        item_2 = "Gummy Bears"
        with pytest.raises(TypeError):
            item_1 > item_2


    def test_ge_true(self):
        item_1 = Cookie('Chocolate Chip', 12, 2)
        item_2 = Candy('Gummy Bears', 1, 1)
        assert item_1 >= item_2


    def test_ge_false(self):
        item_1 = Cookie('Chocolate Chip', 12, 1)
        item_2 = Candy('Gummy Bears', 1, 2)
        assert not item_1 >= item_2


    def test_ge_type_error(self):
        item_1 = Cookie('Chocolate Chip', 12, 1)
        item_2 = "Gummy Bears"
        with pytest.raises(TypeError):
            item_1 >= item_2


    def test_le_true(self):
        item_1 = Cookie('Chocolate Chip', 12, 1)
        item_2 = Candy('Gummy Bears', 1, 2)
        assert item_1 <= item_2


    def test_le_false(self):
        item_1 = Cookie('Chocolate Chip', 12, 2)
        item_2 = Candy('Gummy Bears', 1, 1)
        assert not item_1 <= item_2


    def test_le_type_error(self):
        item_1 = Cookie('Chocolate Chip', 12, 2)
        item_2 = "Gummy Bears"
        with pytest.raises(TypeError):
            item_1 <= item_2
