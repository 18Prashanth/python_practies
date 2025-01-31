# Inheritance = Allows a class to inherit attributes and methods from another class
# Helps with code reusability and extensibility
# class child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class dog(Animal):
    pass


class cat(Animal):
    pass


class mouse(Animal):
    pass


dog = dog("Scooby")
cat = cat("Garfield")
mouse = mouse("Mickey")

print(dog.name)
print(dog.is_alive)
