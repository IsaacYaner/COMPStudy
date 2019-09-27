from collections import defaultdict

class InvalidQuantityError(Exception):
    pass

class Order:
    def __init__(self):
        self._line_items = defaultdict(int)
        self._purchased = False

    def add_to_order(self, item_code, qty):
        self._validate_qty(self._line_items[item_code] + qty)
        self._line_items[item_code] += qty

    def update(self, item_code, qty):
        self._validate_qty(qty)
        self._line_items[item_code] = qty

    def remove(self, item_code):
        del self._line_items[item_code]

    def tabulate_order(self, inventory):
        """ Returns a formatted table """
        cart_items = []
        total_cost = 0
        for i in self._line_items.items():
            item = inventory.get_item(i[0])
            cost = item.price * i[1]
            total_cost += cost
            cart_items.append((item, i[1], cost))

        table = {
            'items': cart_items,
            'total': total_cost
        }
        return table

    def purchase_order(self, inventory):
        self._purchased = True

    def _validate_qty(self, qty):
        if qty < 1:
            raise InvalidQuantityError(f'Cannot have a non-positive quantity. Qty: {qty}')
        if qty > 10:
            raise InvalidQuantityError(f'Cannot have more than 10 units of a single product in cart. Qty: {qty}')

    @property
    def purchased(self):
        return self._purchased
