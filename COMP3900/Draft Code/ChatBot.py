from random import randint

# Bot->mode->mode->mode->mode

# A very basic Bot
class Bot():
    def __init__(self, basemode = None):
        # Change this mode() to other class later
        '''
        Use self.mode and self.stack to switch mode
            between base mode and specific mode
        '''
        if basemode == None:
            self.mode = Mode(self)
        else:
            self.mode = basemode
        self.stack = []
        pass

    def reply(self, text):

        reply = self.mode.reply(text)
        return reply

    def switch(self, token=None):
        if token == 'pop':
            self.pop()
        self.stack.append(self.mode)
        self.mode = self.mode.switch(token)
        return self.mode

    def pop(self):
        self.mode = self.stack.pop()
        return 

class Mode():
    def __init__(self, parent):
        '''
        A mode can produce submode and store in derive
            to implement the context functionality.
        '''
        self.parent = parent
        self.derive = None
        self.response = []
        self.response.append("This is Basic mode")
        pass

    def reply(self, text):
        if self.derive != None:
            return self.derive.reply(text)

        if text == 'add':
            return self.switch()

        if text == 'pop':
            return self.switch('pop')

        border = len(self.response) - 1
        replyIndex = randint(0, border)
        return self.response[replyIndex]

    def switch(self, token=None):
        if token == 'pop':
            return self.parent.pop()
        self.derive = demoMode(self)
        return 'Add first sublayer.'

    def pop(self):
        if self.derive == None:
            return None
        if self.derive.pop() == None:
            self.derive = None
        return 'return to last mode.'

class demoMode(Mode):
    def __init__(self, parent, token=0):
        self.parent = parent
        self.derive = None
        self.response = []
        self.token = token
        self.response.append("This is Demo Mode "+str(token))

    def switch(self, token=None):
        if token == 'pop':
            return self.parent.pop()
        self.derive = demoMode(self, self.token+1)
        return 'Switch to mode ' + str(self.token+1)

    def pop(self):
        if self.derive == None:
            return None
        if self.derive.pop() == None:
            self.derive = None
        return 'return to mode ' + str(self.token)    

bot = Bot()
text = input()
print("The keywords are add and pop, please try")
print("add: create a submode")
print("Stop by typing stop.")
while text != "stop":
    reply = bot.reply(text)
    print(reply)
    text = input()

