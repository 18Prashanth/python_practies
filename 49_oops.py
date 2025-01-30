# object = A "bundel" of related attributes (variables) and methods (functions)
#           Ex. phone, cup, NoteBook
#           you need a "class" to create many get_objects()

# class = (blueprint) used to design the structure and layout of an object

from car import car

car1 = car("Mustang", 2024, "red", False)
car2 = car("Corvvette", 2025, "blue", True)
car3 = car("charger", 2026, "yellow", True)

car3.describe()


# print(car1.model)
# print(car1.year)
# print(car1.color)
# print(car1.for_sale)

# print()

# print(car1.model)
# print(car1.year)
# print(car1.color)
# print(car1.for_sale)

# car1.drive()
# car1.stop()
