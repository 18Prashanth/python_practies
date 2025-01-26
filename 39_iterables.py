# Iterables = An object/collection thar can return its elements one at a time,
# allowing it to be iterated over in a loop

# numbers = [1, 2, 3, 4, 5]

# for number in reversed(numbers):
#     print(number, end="-")


# example - 2 --sets cannot be reverseble
# fruits = {"apple", "orange", "banana", "coconut"}

# for fruit in fruits:
#     print(fruit)


# example 3
# name = "Prasi gowda"

# for character in name:
#     print(character, end="")

# example 4
my_dictionary = {"A": 1, "B": 2, "C": 3}

for key, value in my_dictionary.items():
    print(f"{key}: {value}")
