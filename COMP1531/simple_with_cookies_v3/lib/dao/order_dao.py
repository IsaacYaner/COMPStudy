from abc import ABC, abstractmethod
import pickle

from lib.order import Order

class OrderDAO(ABC):
    @abstractmethod
    def create_new_order(self):
        pass

    @abstractmethod
    def get_order(self, id):
        pass

    @abstractmethod
    def save_data(self):
        pass

    @abstractmethod
    def load_data(cls):
        pass


class OrderManager(OrderDAO):
    def __init__(self):
        # List of completed orders
        self._orders = []

    def create_new_order(self):
        self._orders.append(Order())
        return len(self._orders) - 1

    def get_order(self, id):
        return self._orders[id]


    def save_data(self):
        with open('orders.dat', 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def load_data(cls):
        try:
            with open('orders.dat', 'rb') as file:
                order_manager = pickle.load(file)
        except IOError:
            order_manager = OrderManager()
        return order_manager
