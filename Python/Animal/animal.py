class Animal(object):               # define a new Animal class
    def __init__(self, name):
      # define attributes
      self.name = name
      self.health = 100
    # define methods
    def walk(self):
      self.health -= 1
    def run(self):
      self.health -= 5
    def displayhealth(self):
        print(self.name, self.health)
animal1 = Animal("Bunny")
animal1.walk()
animal1.walk()
animal1.walk()
animal1.run()
animal1.run()
animal1.displayhealth()
