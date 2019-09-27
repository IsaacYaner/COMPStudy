import pytest
from lib.dao.inventory_dao import Warehouse
from lib.products import *

class TestSearch:
    def setup_method(self):
        self._warehouse = Warehouse()
        self._warehouse.add_item(Shirt("Cool Shirt", 25.2, 'S', 'Red'))
        self._warehouse.add_item(Shirt("Oversized Shirt", 50.59, 'XL', 'Green'))
        self._warehouse.add_item(Shirt("Gucci Mane", 713.1, 'M', 'Brown/Orange'))
        self._warehouse.add_item(Shirt("Basics Range", 9.95, 'S', 'White'))
        self._warehouse.add_item(Shirt("Google Attire", 25.2, 'S', 'Multi'))

        self._warehouse.add_item(Pants("Basics Range", 19.95, 'S', 'White'))
        self._warehouse.add_item(Pants("Jeans", 70.0, 'M', 'Jeans'))

        self._warehouse.add_item(Accessories("Blue Cool Earrings", 70.35, 'OneSize', 'Blue'))
        self._warehouse.add_item(Accessories("Schooler Hat", 19.95, 'M', 'Yellow'))

    #### User Story 1 - General search ####
    def test_general_search(self):
        self._warehouse = Warehouse()
        self._warehouse.add_item(Shirt("Cool Shirt", 25.2, 'S', 'Red'))
        self._warehouse.add_item(Shirt("Oversized Shirt", 50.59, 'XL', 'Green'))
        self._warehouse.add_item(Shirt("Gucci Mane", 713.1, 'M', 'Brown/Orange'))
        self._warehouse.add_item(Shirt("Basics Range", 9.95, 'S', 'White'))
        self._warehouse.add_item(Shirt("Google Attire", 25.2, 'S', 'Multi'))

        self._warehouse.add_item(Pants("Basics Range", 19.95, 'S', 'White'))
        self._warehouse.add_item(Pants("Jeans", 70.0, 'M', 'Jeans'))

        self._warehouse.add_item(Accessories("Blue Cool Earrings", 70.35, 'OneSize', 'Blue'))
        self._warehouse.add_item(Accessories("Schooler Hat", 19.95, 'M', 'Yellow'))
        text = "Cool"
        result = self._warehouse.search_all(text)
        for i in result:
            print(i)
            print(i._name, i._item_code, i._colour, i._price, i._size)
        # for i in result:
        #     assert(text in i.name)

ts = TestSearch()
ts.test_general_search()