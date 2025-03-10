# static methods = A method that belong to a class rather than any object from that class (instances)
# usually used for general utility function
# Instance methods = Best for operation on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["manager", "cashier", "cook", "Janitor"]
        return position in valid_positions


employee1 = Employee("Shivakumar", "Manager")
employee2 = Employee("Prashanth", "Cashier")
employee3 = Employee("Shama", "Cook")

print(Employee.is_valid_position("Rook scientiest"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
