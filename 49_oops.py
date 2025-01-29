# object = A "bundel" of related attributes (variables) and methods (functions)
#           Ex. phone, cup, NoteBook
#           you need a "class" to create many get_objects()

# class = (blueprint) used to design the structure and layout of an object

class car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale


car1 = car("Mustang", 2024, "red", False)
car2 = car("Corvvette", 2025, "blue", True)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

print()

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)
