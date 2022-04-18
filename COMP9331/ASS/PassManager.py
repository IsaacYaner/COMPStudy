class PassManager():
    def __init__(self, path='credentials.txt'):
        self.path = path
        self.user = {}
        self.online = []

    # Load authentication info from self.path
    def read(self):
        with open(self.path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                data = line.split()
                if len(data) == 2:
                    self.user[data[0]] = data[1]

    # Save into self.path
    def save(self):
        with open(self.path, 'w') as f:
            for user in self.user:
                f.write(f'{user} {self.user[user]}\n')
            f.write('\n')

    # Return whether useername is stored in the system
    def exist(self, username):
        return username in self.user

    # Return whether the username and password match
    def match(self, username, password):
        if self.exist(username):
            return password == self.user[username]

    # Return the login status of username
    def isOnline(self, username):
        return username in self.online
        
    # Return list of online users
    def onlineUsers(self):
        return len(self.online)

    # Login function, create a new account of password and login
    #   if the account is not registered
    def login(self, username, password):
        if not self.exist(username):
            self.add(username, password)
            self.online.append(username)
            return True
        if self.match(username, password):
            self.online.append(username)
            return True
        return False

    # Logout
    def logout(self, username):
        self.online.remove(username)

    # Add a new user to the system
    def add(self, username, password):
        self.user[username] = password
        self.save()