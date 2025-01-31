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
        print(f"{self.name} is asleep")


class dog(Animal):
    def speak(slef):
        print("WOOF!")


class cat(Animal):
    def speak(slef):
        print("MEOW!")


class mouse(Animal):
    def speak(slef):
        print("SQUEEK!")


dog = dog("Scooby")
cat = cat("Garfield")
mouse = mouse("Mickey")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
dog.speak()
