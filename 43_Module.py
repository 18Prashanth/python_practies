# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up alarge program reusable seperate files


# import math
# import math as m
# from math import pi
# from math import e

# a, b, c, d = 1, 2, 3, 4
# print(e ** a)
# print(e ** b)
# print(e ** c)
# print(e ** d)

# ---------------------------------\The below module import from the file 44_example43.py--
import example

# result = example43.pi()
result = example.square(3)
result = example.cube(3)
result = example.circumference(3)
result = example.area(3)
print(result)
