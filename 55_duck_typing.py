# "Duck typing" = Another way to achive polymorphism besides Inheritance
# object mustr have the minimum necessary attributes/methods
# "If it looks like a duck and quacks like a duck, it must be a duck"

class Animal:
    alive = True


class Dog(Animal):
    def speak(self):
        print("WOOF!")


class Cat(Animal):
    def speak(self):
        print("MEOW!")


class Car:

    def speak(self):
        print("HONK!")


animals = [Dog(), Cat(), Car()]


for animal in animals:
    animal.speak()
    print(Animal.alive)
