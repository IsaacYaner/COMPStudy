class Animal:
    'Parent class for all animals'
    def __init__(self,kind,species,lifespan):
        self._kind = kind
        self._species = species
        self._lifespan = lifespan

class Bird(Animal):
    'A common class for all birds'
    def __init__(self,kind,lifespan,food,region,species="Aves"):
        Animal.__init__(self,kind,species,lifespan)
        self._food = food
        self._region = region
        
    def __str__(self):
        return "{0} is a {1} and it lives in the {2} region".format(self._kind,self._species,self._region)
        
class Dog(Animal):
    'A common class for all dogs'
    def __init__(self,kind,species,lifespan,family_dog):
        Animal.__init__(self,kind,species,lifespan)
        self._family_dog = family_dog

    def __str__(self):
        return "{0} is a {1} and it lives for {2} years".format(self._kind,self._species,self._lifespan)

dog = Dog("Colies","Canis Lupis",10,True)

#Do not have to pass species, uses the default value
penguin = Bird("penguin",3,"fish","Antartic")

print(penguin)  # invokes __str__()
print(dog)