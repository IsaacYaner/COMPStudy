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
        self.threads[title].dump()
        
        return f'Thread {title} created'

    def post(self, name, title, message):
        if not self.exist(title):
            raise ExistenceError(f'Thread {title} doesn\'t exist')
        self.threads[title].addPost(name, message)
        
        return f'Message posted to {title} thread'

    def delete(self, name, title, number):
        # Check for errors
        if not self.exist(title):
            raise ExistenceError(f'Thread {title} doesn\'t exist')
        if number <= 0 or number > self.threads[title].length():
            raise ExistenceError(f'Post number {number} doesn\'t exist')
        if name != self.threads[title].getAuthor(number):
            raise AccessError(f'The message belongs to another user and cannot be edited')
        
        # Call delepost directly
        self.threads[title].deletePost(number)
        return f'The message has been deleted'
    
    def edit(self, name, title, number, message):
        if not self.exist(title):
            raise ExistenceError(f'Thread {title} doesn\'t exist')
        if number <= 0 or number > self.threads[title].length():
            raise ExistenceError(f'Post number {number} doesn\'t exist')
        if name != self.threads[title].getAuthor(number):
            raise AccessError(f'The message belongs to another user and cannot be edited')
        
        self.threads[title].editPost(number, message)
        return f'Message {number} edited'
    
    def listTitles(self):
        if len(self.threads) == 0:
            return 'No threads to list'
        return '\n'.join(self.threads.keys())
        
    def readTitle(self, title):
        if not self.exist(title):
            raise ExistenceError(f'Thread {title} doesn\'t exist')
        return self.threads[title].dumps()
    
    def upload(self, name, title, filename):
        if not self.exist(title):
            raise ExistenceError(f'Thread {title} doesn\'t exist')
        if filename in self.threads[title].files:
            raise ExistenceError(f'File {filename} already existed')
        self.threads[title].upload(name, filename)
        return f'{filename} uploaded to {title} thread'
        
    def download(self, title, filename):
        if not self.exist(title):
            raise ExistenceError(f'Thread {title} doesn\'t exist')
        if filename not in self.threads[title].files:
            raise ExistenceError(f'File does not exist in Thread {title}')
        return f'{filename} successfully downloaded'
        
    def remove(self, name, title):
        if not self.exist(title):
            raise ExistenceError(f'Thread {title} doesn\'t exist')
        if name != self.threads[title].username:
            raise AccessError(f'Thread cannot be removed')
        self.threads[title].remove()
        del self.threads[title]
        return f'Thread {title} removed'


        
