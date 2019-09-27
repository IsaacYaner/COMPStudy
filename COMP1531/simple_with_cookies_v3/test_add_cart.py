import pytest
from lib.dao.inventory_dao import Warehouse
from lib.products import *
from lib.cart import Cart, InvalidQuantityError

class TestAddCart:
    def test_add_cart(self):
        cart = Cart()
        cart.add_to_cart(0, 1)
        # What do you want to test here?
        assert(len(cart._line_items) == 1)

    def test_add_cart_nonpositive(self):
        cart = Cart()
        with pytest.raises(InvalidQuantityError):
            cart.add_to_cart(0, 0)


    def test_add_cart_exceessive(self):
        cart = Cart()
        with pytest.raises(InvalidQuantityError):
            cart.add_to_cart(0, 11)
