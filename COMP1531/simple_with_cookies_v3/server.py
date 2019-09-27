from flask import Flask
from lib.dao.inventory_dao import Warehouse
from lib.dao.order_dao import OrderManager
from lib.shopping_data import OnlineShoppingData


app = Flask(__name__)
app.secret_key = 'very-secret-123'  # Used to add entropy

# Loads data
warehouse = Warehouse.load_data()
order_manager = OrderManager.load_data()
# warehouse, order_manager = OnlineShoppingData.load_data()
