from lib.dao.inventory_dao import Warehouse
from lib.dao.order_dao import OrderManager
from lib.order import Order
from lib.products import *


class OnlineShoppingData:
    @classmethod
    def load_data(cls):
        warehouse = Warehouse()
        a1 = Accessories("gloves", 10, "S", "Blue")
        a2 = Accessories("kids gloves", 10, "S", "Red")
        a3 = Accessories("Glasses", 25, "M", "Pink")
        a4 = Accessories("Scarf", 50, "L", "Yellow")
        misc = Miscellaneous("Torch", 100, "1x2x3", "100kg")

        warehouse.add_item(a1)
        warehouse.add_item(a2)
        warehouse.add_item(a3)
        warehouse.add_item(a4)
        warehouse.add_item(misc)

        order_manager = OrderManager()

        cart_id = order_manager.create_new_order()
        cart = order_manager.get_order(cart_id)
        cart.add_to_order(0, 10)
        cart.add_to_order(1, 3)
        cart.add_to_order(2, 5)
        cart.add_to_order(4, 6)
        cart.purchase_order(warehouse)

        cart_id = order_manager.create_new_order()
        cart = order_manager.get_order(cart_id)
        cart.add_to_order(0, 1)
        cart.purchase_order(warehouse)

        return warehouse, order_manager
