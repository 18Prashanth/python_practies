# Multiple inheritance = inherit from more than one parent class
#                       C(A,B)

# Multi level inheritance = inherit from a parent which inherits from another parent()
#                            C(B) <- B(A) <- A

class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"This {self.name} is eating")

    def sleep(self):
        print(f"This {self.name} is sleeping")


class prey(Animal):
    def flee(self):
        print(f"This {self.name} is fleeing")


class Predator(Animal):
    def hunt(self):
        print(f"This {self.name} is hunting")


class Rabbit(prey):
    pass


class Hawk(Predator):
    pass


class Fish(prey, Predator):
    pass


rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.eat()
