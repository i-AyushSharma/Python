class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def make_sound(self):
        print("bark!")

d = Dog("Dog", "Doberman")
d.make_sound()
a = Animal("Dog", "Dog")
a.make_sound()