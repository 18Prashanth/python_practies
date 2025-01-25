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
# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")


# display_name("Mr", "Prashanth", "gowda")


# ------------**kwargs-------
# def print_address(**kwargs):
#     # print(type(kwargs))
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")


# print_address(street="Lebus street",
#               city="London",
#               state="England",
#               zip="N17 9FQ")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")
    print()

    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')}, {kwargs.get('state')}, {kwargs.get('zip')}")


shipping_label("Dr", "Prashanth", "Gowda", "III",
               street="Lebus street",
               city="London",
               state="England",
               zip="N17 9FQ")
