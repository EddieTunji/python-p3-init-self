class Dog:
    pass

fido = Dog()

snoopy = Dog()

fido.breed = "Dalmatian"
snoopy.breed = "Beagle"

fido.breed
print(fido.breed)
print(snoopy.breed)

class Dog:
    def __init__(self, name):
        print(f"{name} is born!")

    def bark(self):
        print("Woof!")

    def showing_self(self):
        return self

fido = Dog("Fido")
snoopy = Dog("Snoopy")
fido.showing_self()
fido is fido.showing_self()
snoopy is snoopy.showing_self()

class Dog:
    def __init__(self, name):
        self.name = name
        
        def bark(self):
            print("Woof!")

fido = Dog("Fido")
fido.name
snoopy = Dog("Snoopy")
snoopy.name

class Dog:
    def __init__(self, name):
        self.name = name

fido.owner = "Sophie"
print(fido.owner)

def adopt(dog, owner_name):
        dog.owner = owner_name

adopt(fido, "Sophie")
print(fido.owner)

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Woof!")

    def get_adopted(self, owner_name):
        self.owner = owner_name

fido = Dog("Fido")
fido.get_adopted("Tunji")
print(fido.owner)

class Dog:
    def  __init__ (self, name, favorite_toy="Any"):
        self.name = name
        self.favorite_toy = favorite_toy
        
fido = Dog("Fido")
print(fido.favorite_toy)

snoopy = Dog("Snoopy", "Tennis Ball")
print(snoopy.favorite_toy)
        

