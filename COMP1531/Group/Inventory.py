class inventory:
    def __init__(self, stock):
        self._stock = stock

    def add(self, name, value = 0):
        self._stock[name] = value

    def increment(self, name, value):
        self._stock[name] = self._stock[name]+value
        warn()

    def decrement(self, name, value):
        self._stock[name] = self._stock[name]+value
        warn()

    def modify(self, name, value):
        self._stock[name] = self._stock[name]+value
        warn()

    def validate(self, order, value):
        for name in order:
            if self._stock[name] < value:
                return 0
        return 1

    def warn():
        for name in self._stock:
            if self._stock[name] < 10:
                #warn
                return
