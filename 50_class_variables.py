# class variables = shared among all instances of a class
# defined outside the constructor
# Allow you to share data among all objects created from that class

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = student("Prashanth", 30)
student2 = student("Patrick", 35)

print(student1.name)
print(student2.age)
