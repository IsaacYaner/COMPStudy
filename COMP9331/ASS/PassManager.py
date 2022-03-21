from numpy import mat
from pexpect import EOF


class PassManager():
    def __init__(self, path='credentials.txt'):
        self.path = path
        self.user = {}
        self.online = []

    def read(self):
        with open(self.path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                data = line.split()
                if len(data) == 2:
                    self.user[data[0]] = data[1]

    def save(self):
        with open(self.path, 'w') as f:
            for user in self.user:
                f.write(f'{user} {self.user[user]}\n')
            f.write('\n')

    def exist(self, username):
        return username in self.user

    def match(self, username, password):
        if self.exist(username):
            return password == self.user[username]

    def isOnline(self, username):
        return username in self.online
        
    def login(self, username, password):
        if not self.exist(username):
            self.add(username, password)
            self.online.append(username)
            return True
        if self.match(username, password):
            self.online.append(username)
            return True
        return False

    def add(self, username, password):
        self.user[username] = password
        self.save()