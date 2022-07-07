class Cache:
    def __init__(self):
        self.count = 0
        self.lock = False

    def update(self, new_count):
        if not self.lock:
            self.count = new_count

'''
For simplicity, B and modding is elips left out
'''
class Counter:
    caches = []
    def __init__(self, num_readers):
        self.count = 0
        for i in range(num_readers):
            self.caches.append(Cache())

    def increment(self):
        self.count += 1
        for c in self.caches:
            c.update(self.count)

class Writer:
    def __init__(self, counter):
        self.counter = counter

    def write(self):
        self.counter.increment()

class Reader:
    def __init__(self, cache):
        self.cache = cache

    def read(self):
        self.cache.lock = True
        self.serial_read()
        self.cache.update(counter)
        self.cache.lock = False

    def serial_read():
        #Read content
        return


