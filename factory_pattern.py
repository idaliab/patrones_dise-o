# factory_pattern.py
class Dog:
    """"A simple dog class"""
    def __init__(self, name):
        self._name = name
    def speak(self):
        return "Woof!"
class Cat:
    """"A simple cat class"""
    def __init__(self, name):
        self._name = name
    def speak(self):
        return "Meow!"
class Duck:
    """"A simple duck class"""
    def __init__(self, name):
        self._name = name
    def speak(self):
        return "Quack!"
    
def get_pet(pet="dog"):
    """The factory method"""
    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"), duck=Duck("Love"))
    return pets[pet]

d = get_pet()
print(d._name, d.speak())
c = get_pet("cat")
print(c._name, c.speak())
duck = get_pet("duck")
print(duck._name, duck.speak())

    
