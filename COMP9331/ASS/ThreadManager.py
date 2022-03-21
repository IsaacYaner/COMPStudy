from Thread import *
from Errors import *

class ThreadManager():
    def __init__(self):
        self.threads = {}
        pass

    def exist(self, title):
        return title in self.threads

    def create(self, name, title):
        if self.exist(title):
            raise ExistenceError(f'Thread {title} exists')
        self.threads[title] = Thread(title, name)
        return f'Thread {title} created'

    def post(self, name, title):
        pass
        
