class Account:
    def __init__(self,name,bal,min=50.0):
        # instance variables
        self.__name = name
        self.__balance = bal
        self.__min_bal = min
    
    #instance methods
    def withdraw(self,amount):
        self.__balance = self.__balance - amount
    
    #accessor and mutator methods
    def get_name(self):
        return self.__name
    def get_balance(self):
        return self.__balance
    def set_name(self,name):
        self.__name = name
    
    #overriding method __str__()
    def __str__(self):
        return "{0}'s account has a balance of: {1}".format(self.__name, self.__balance)

class SavingsAccount(Account):
    def __init__(self,name,bal,min=50.0):
        
        # instance variables
        super().__init__(name,bal,min)
        self.__saver_interest = 0.05

    def __str__(self):
        return super().__str__() + " with an interest of: {0}".format(self.__saver_interest * self.get_balance())

#client code
a1=Account("sam",300,50)
print(a1)

a2=SavingsAccount("mary",500,10)
print(a2)

