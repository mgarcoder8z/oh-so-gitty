from animal import Animal
class Dog(Animal):
    def __init__(self, name):
      # define attributes
      self.name = name
      self.health = 150
    def pet(self):
      self.health += 5
class Dragon(Animal):
    def __init__(self, name):
      # define attributes
      self.name = name
      self.health = 170
    def fly(self):
      self.health -= 10
dog1 = Dog("Fido")
dog1.walk()
dog1.walk()
dog1.walk()
dog1.run()
dog1.run()
dog1.pet()
dog1.displayhealth()
dragon1 = Dragon("Draco")
dragon1.walk()
dragon1.walk()
dragon1.walk()
dragon1.run()
dragon1.run()
dragon1.fly()
dragon1.fly()
dragon1.displayhealth()
