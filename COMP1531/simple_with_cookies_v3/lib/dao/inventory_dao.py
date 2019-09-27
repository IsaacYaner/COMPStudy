import pickle

from lib.products import *


class InventoryDAO(ABC):
    @abstractmethod
    def search_all(self, name):
        pass

    @abstractmethod
    def search_cat(self, cat, name):
        pass

    @abstractmethod
    def search_subcat(self, subcat, name):
        pass

    @abstractmethod
    def add_item(self, item):
        pass

    @abstractmethod
    def get_item(self, code):
        pass

    @abstractmethod
    def get_all_items(self):
        pass

    @abstractmethod
    def max_id(self):
        pass

    @abstractmethod
    def save_data(self):
        pass

    @abstractmethod
    def load_data(cls):
        pass


class Warehouse(InventoryDAO):
    def __init__(self):
        # Full list of items -> think of OO DB
        self._items = []
        # Mapping for quick access of the id->items
        self._mapping = {}

    def search_all(self, name):
        return [i for i in self._items
                if name.lower() in i.name.lower()
                ]

    def search_cat(self, cat, name):
        # Category search
        return [i for i in self._items
                if name.lower() in i.name.lower()
                and i.__class__.__bases__[0].__name__ == cat
                ]

    def search_subcat(self, subcat, name):
        # Subcategory search
        return [i for i in self._items
                if name.lower() in i.name.lower()
                and i.__class__.__name__ == subcat
                ]

    def update(self, id, **kwargs):
        item = self._mapping.get(id)
        if item is None:
            return

        # Sets item values (asserting that the attributes exist)
        for k, v in kwargs.items():
            assert (hasattr(item, k))
            setattr(item, k, v)

    def add_item(self, item):
        if item.item_code in self._mapping:
            # Shouldn't ever happen
            raise NotImplementedError("Duplicate name error")

        self._items.append(item)
        self._mapping[item.item_code] = item

    def get_item(self, code):
        return self._mapping.get(code)

    def get_all_items(self):
        return self._items

    def max_id(self):
        return max([x.item_code for x in self._items])

    def get_items(self, ids):
        return [i for i in self._items if i.item_code in ids]

    def save_data(self):
        with open('inventory.dat', 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def load_data(cls):
        try:
            with open('inventory.dat', 'rb') as file:
                warehouse = pickle.load(file)
            Product.set_id(warehouse.max_id())
        except IOError:
            warehouse = Warehouse()
        return warehouse
