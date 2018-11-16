#abstract_factory.py
class Dog:
    """One of the objects to be returned"""
    def speak(self):
        return "Woof!"
    def __str__(self):
        return "Dog"
class Cat:
    """One of the objects to be returned"""
    def speak(self):
        return "Meow!"
    def __str__(self):
        return "Cat"
    
class DogFactory:
    """Concrete factory"""
    def get_pet(self):
        """Returns a Dog object"""
        return Dog()
    def get_food(self):
        """Returns a Dog Food object"""
        return "Dog food"
class CatFactory:
    """Concrete factory"""
    def get_pet(self):
        """Returns a Cat object"""
        return Dog()
    def get_food(self):
        """Returns a Cat Food object"""
        return "Cat food"

class PetStore:
    """PetStore houses our Abstract Factory"""
    def __init__(self, pet_factory=None):
        """Pet factory is our Abstract Factory"""
        self._pet_factory = pet_factory
    def show_pet(self):
        """Utility method to display the details of the objects returned by the factory"""
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()
        print("Our pet is '{}'!".format(pet))
        print("Our pet says hello by '{}'!".format(pet.speak()))
        print("Its food is '{}'!".format(pet_food))
    def change_factory(self, pet_factory=DogFactory()):
        self._pet_factory = pet_factory

# Create a Concrete Factory
factory = DogFactory()
#Create a pet store housing our Abstract Factory
shop = PetStore(factory)
# Invoke the utility method to show the details of our pet
shop.show_pet()

cat_factory = CatFactory()
shop.change_factory(cat_factory)
shop.show_pet()


        
