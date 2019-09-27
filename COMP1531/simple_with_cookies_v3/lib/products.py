from abc import ABC, abstractmethod


class Product(ABC):
    # This needs to be properly initialised if we are using persistent data
    __id = -1

    @abstractmethod
    def __init__(self, name, price):
        self._item_code = self.generate_id()
        self._name = name
        self._price = float(price)

    @property
    def item_code(self):
        return self._item_code

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    def generate_id(self):
        Product.__id += 1
        return Product.__id

    @classmethod
    def set_id(cls, id):
        cls.__id = id


class Clothing(Product):
    def __init__(self, name, price, size, colour):
        super().__init__(name, price)
        self._size = size
        self._colour = colour

    @property
    def size(self):
        return self._size

    @property
    def colour(self):
        return self._colour


class Camping(Product):
    def __init__(self, name, price, dimension, weight):
        super().__init__(name, price)


class Shirt(Clothing):
    # Possible extra attribute: Style
    def __init__(self, name='none', price=0.0, size='S', colour='unknown'):
        super().__init__(name, price, size, colour)

    def get_size(self):
        return self._size

    def get_colour(self):
        return self._colour


class Pants(Clothing):
    # Possible extra attribute: Material
    pass


class Accessories(Clothing):
    # Possible extra attribute: Number per pack
    def __init__(self, name='none', price=0.0, size='S', colour='unknown'):
        super().__init__(name, price, size, colour)

    def get_size(self):
        return self._size

    def get_colour(self):
        return self._colour


class Electrical(Camping):
    pass


class Miscellaneous(Camping):
    pass


# Maps the name to the class so we can interface between Web and Python
CATEGORIES = {
    x.__name__: x for x in Product.__subclasses__()
}

CLOTHING = {
    x.__name__: x for x in Clothing.__subclasses__()
}

CAMPING = {
    x.__name__: x for x in Camping.__subclasses__()
}

# Merges the two dicts together, using dictionary unpacking
ALL_ITEMS = {**CLOTHING, **CAMPING}
