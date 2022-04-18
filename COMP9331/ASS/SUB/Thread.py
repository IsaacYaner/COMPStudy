import enum
import os

# Core function of a forum
class Thread():
    def __init__(self, title, username):
        self.title = title
        self.username = username
        self.posts = []
        self.files = []
        self.objects = []
        self.dump()
    
    # Return snumber of posts
    def length(self):
        return len(self.posts)

    # Load from local file
    def load(self):
        with open(self.title, 'r') as f: 
            content = f.readlines()
        self.username = content[0]
        for post in content[1:]:
            post = post.split(': ')
            name = post[0].split()[1]
            message = post[:-1]                     # Omit the '\n'
            self.posts.append([name, message])
    
    # Return author of n-th post
    def getAuthor(self, number):
        return  self.posts[number-1][0]

    # Add post to the post lis, stored in a [name, message] structure
    #   And then save
    def addPost(self, name, message):
        self.posts.append([name, message])
        # Also add to objects list
        self.objects.append(None)
        self.savePost()
        pass
    
    # Delete nth post from self.posts
    # And then delete it from object list
    def deletePost(self, number):
        self.posts.pop(number-1)
        i = 0       # i stands for nth post
        nth = 0     # nth stands for nth object
        while i <= number-1:
            if self.objects[nth] is None:
                if i == number-1:
                    break
                i+=1
            nth+=1
        self.objects.pop(nth)
        self.dump()

    # Edit post, and save
    def editPost(self, number, message):
        self.posts[number-1][1] = message
        self.dump()

    # Save the last post only
    def savePost(self):
        with open(self.title, 'a') as f:
            num = len(self.posts)
            author = self.posts[-1][0]
            message = self.posts[-1][1]
            post = f'{num} {author}: {message}\n'
            f.write(post)

    # Save this class into a string as specified by the specs
    def dumps(self, suppress=True):
        result = ''
        if not suppress:
            result += self.username + '\n'
        
        # For the case that the first object is a file instead of post
        nth = 0
        while nth<len(self.objects) and self.objects[nth] is not None:
            result += self.objects[nth][1]
            nth+=1
        
        # Print all objects in the middle
        for i, post in enumerate(self.posts):
            while nth<len(self.objects) and self.objects[nth] is not None:
                result += self.objects[nth][1]
                nth+=1
            
            num = i + 1
            author = self.posts[i][0]
            message = self.posts[i][1]
            result += f'{num} {author}: {message}\n'
            nth+=1

        # print the last object if it's a file
        while nth<len(self.objects) and self.objects[nth] is not None:
            result += self.objects[nth][1]
            nth+=1
        return result[:-1]

    # Save the class locally as specified in the specs
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
    
    # Upload a file and update object list
    def upload(self, name, filename):
        self.files.append(filename)
        self.objects.append([name, f'{name} uploaded {filename}\n'])
        self.dump()
    
    # remove all associated files
    def remove(self):
        os.remove(self.title)
        for fn in self.files:
            os.remove(self.title+'-'+fn)