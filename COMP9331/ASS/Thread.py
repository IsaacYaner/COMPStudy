import enum
import os

class Thread():
    def __init__(self, title, username):
        self.title = title
        self.username = username
        self.posts = []
        self.files = []
        self.objects = []
        self.dump()
    
    def length(self):
        return len(self.posts)

    def load(self):
        with open(self.title, 'r') as f: 
            content = f.readlines()
        self.username = content[0]
        for post in content[1:]:
            post = post.split(': ')
            name = post[0].split()[1]
            message = post[:-1]                     # Omit the '\n'
            self.posts.append([name, message])
    
    def getAuthor(self, number):
        return  self.posts[number-1][0]

    def addPost(self, name, message):
        self.posts.append([name, message])
        self.objects.append(None)
        self.savePost()
        pass

    def deletePost(self, number):
        self.posts.pop(number-1)
        i = 0       # i stands for nth post
        nth = 0     # nth stands for nth object
        while i < number-1:
            if self.objects is None:
                i+=1
            nth+=1
        self.posts.pop(nth)
        self.dump()

    def editPost(self, number, message):
        self.posts[number-1][1] = message
        self.dump()

    def savePost(self):
        with open(self.title, 'a') as f:
            num = len(self.posts)
            author = self.posts[-1][0]
            message = self.posts[-1][1]
            post = f'{num} {author}: {message}\n'
            f.write(post)

    def dumps(self, suppress=True):
        result = ''
        if not suppress:
            result += self.username + '\n'
        
        nth = 0
        while nth<len(self.objects) and self.objects[nth] is not None:
            result += self.objects[nth][1]
            nth+=1
        
        for i, post in enumerate(self.posts):
            while nth<len(self.objects) and self.objects[nth] is not None:
                result += self.objects[nth][1]
                nth+=1
            
            num = i + 1
            author = self.posts[i][0]
            message = self.posts[i][1]
            result += f'{num} {author}: {message}\n'
            nth+=1

        while nth<len(self.objects) and self.objects[nth] is not None:
            result += self.objects[nth][1]
            nth+=1
        return result[:-1]

    def dump(self):
        with open(self.title, 'w') as f:
            f.write(self.username + '\n')
            nth = 0
            while nth<len(self.objects) and self.objects[nth] is not None:
                f.write(self.objects[nth][1])
                nth+=1

            for i, post in enumerate(self.posts):
                while nth<len(self.objects) and self.objects[nth] is not None:
                    f.write(self.objects[nth][1])
                    nth+=1

                num = i + 1
                author = self.posts[i][0]
                message = self.posts[i][1]
                post = f'{num} {author}: {message}\n'
                f.write(post)
                nth+=1

            while nth<len(self.objects) and self.objects[nth] is not None:
                f.write(self.objects[nth][1])
                nth+=1
    
    def upload(self, name, filename):
        self.files.append(filename)
        self.objects.append([name, f'{name} uploaded {filename}\n'])
        self.dump()
    
    def remove(self):
        os.remove(self.title)
        for fn in self.files:
            os.remove(self.title+'-'+fn)