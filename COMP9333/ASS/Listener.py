import json
from logging.config import listen
class Listener():
    def __init__(self):
        pass
    
    def read(self, text):
        self.handle(text)

    def handle(self): 
        pass

class CommandListener(Listener):
    def __init__(self, path='command_format.json'):
        self.command_format_path = path
        with open(path) as f:
            self.commands = json.load(f)

    def handle(self, text):
        # Split the command
        text = text.split()
        # For invalid command
        if len(text) == 0 or text[0] not in self.commands.keys():
            return self.commands['Invalid']
        
        # Process commands
        command = text[0]

        # Invalid Format
        if len(text) != self.commands[command]['length']:
            return self.commands['Error message'].format(command)
        
        

    def store_format(self, path=None):
        if path is None:
            path = self.command_format_path
        with open(path, 'w') as f:
            json.dump(self.commands, f, indent=4)

listener = CommandListener()
data = listener
while(True):
    data.read(input())
 