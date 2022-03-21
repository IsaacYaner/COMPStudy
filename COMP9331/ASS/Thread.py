import enum


class Thread():
    def __init__(self, title, username):
        self.title = title
        self.username = username
        self.posts = []
        self.dump()
    
    def load(self):
        with open(self.title, 'r') as f: 
            content = f.readlines()
        self.username = content[0]
        for post in content[1:]:
            post = post.split(': ')
            name = post[0].split()[1]
            message = post[:-1]                     # Omit the '\n'
            self.posts.append((name, message))
    
    def addPost(self, name, message):
        self.posts.append((name, message))
        self.savePost()
        pass

    def deletePost(self):
        pass

    def savePost(self):
        with open(self.title, 'a') as f:
            num = len(self.posts) - 1
            author = self.posts[-1][0]
            message = self.posts[-1][1]
            post = f'{num} {author}: {message}\n'
            f.write(post)

    def dump(self):
        with open(self.title, 'w') as f:
            f.write(self.username + '\n')
            for i, post in enumerate(self.posts):
                num = i + 1
                author = self.posts[i][0]
                message = self.posts[i][1]
                post = f'{num} {author}: {message}\n'
                f.write(post)