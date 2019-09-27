#User-defined exceptions
class UserInputError(Exception):
        "Raised when the user-name field is invalid"
        pass

#business logic
def validate_user_name(name):
    
    print(len(name))
    if len(name) <1 or len(name) >25 or name.find(' ') != -1: 
                raise UserInputError("user input error")
    # validation successful, do something with the user-name, e.g., add to database
    return True
