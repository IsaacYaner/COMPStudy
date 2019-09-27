from order import Order


class CartManager:

    __id = -1

    @classmethod
    def generate_id(cls):
        CartManager.__id += 1
        return CartManager.__id

class Cart:
    def __init__(self):
        self._id = CartManager.generate_id()
        self._items = []

