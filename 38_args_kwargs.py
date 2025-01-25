# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keybord-arguments
# * unpacking operator
# 1.positional 2.default 3.keyboard 4.ARBITRARY


# def add(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total


# print(add(1, 2, 3))

# example 2
def display_name(*args):
    for arg in args:
        print(arg, end=" ")


display_name("Mr", "Prashanth", "gowda")
