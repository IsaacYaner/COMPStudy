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
        text = "Cool"
        result = self._warehouse.search_all(text)

        for i in result:
            assert(text in i.name)

    def test_general_search_insensitive(self):
        text = "cOOl"
        result = self._warehouse.search_all(text)
        lower_text = text.lower()
        for i in result:
            assert(lower_text in i.name.lower())

    def test_general_search_no_match(self):
        text = "NOT FOUND 123"

        result = self._warehouse.search_all(text)

        assert(len(result) == 0)

    def test_general_search_exact_name(self):
        text = "Schooler Hat"

        result = self._warehouse.search_all(text)
        assert(len(result) == 1)
        for i in result:
            assert(i.name == text)


    #### User Story 2 - Category ####
    def test_cat_search(self):
        text = "Cool"
        result = self._warehouse.search_cat(Clothing.__name__, text)

        for i in result:
            assert(text in i.name)

    def test_cat_search_insensitive(self):
        text = "cOOl"
        result = self._warehouse.search_cat(Clothing.__name__, text)

        lower_text = text.lower()
        for i in result:
            assert(lower_text in i.name.lower())

    def test_cat_search_no_match(self):
        text = "NOT FOUND 123"

        result = self._warehouse.search_cat(Clothing.__name__, text)

        assert(len(result) == 0)

    def test_cat_search_exact_name(self):
        text = "Gucci Mane"
        result = self._warehouse.search_cat(Clothing.__name__, text)
        assert(len(result) == 1)
        for i in result:
            assert(i.name == text)


    #### User Story 2 - Subcategory ####
    def test_subcat_search(self):
        text = "Cool"
        result = self._warehouse.search_subcat(Shirt.__name__, text)

        for i in result:
            assert(text in i.name)

    def test_subcat_search_insensitive(self):
        text = "cOOl"
        result = self._warehouse.search_subcat(Shirt.__name__, text)

        lower_text = text.lower()
        for i in result:
            assert(lower_text in i.name.lower())

    def test_subcat_search_no_match(self):
        text = "NOT FOUND 123"

        result = self._warehouse.search_subcat(Shirt.__name__, text)

        assert(len(result) == 0)

    def test_subcat_search_exact_name(self):
        text = "Gucci Mane"
        result = self._warehouse.search_subcat(Shirt.__name__, text)
        assert(len(result) == 1)
        for i in result:
            assert(i.name == text)
