# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keybord-arguments
# * unpacking operator
# 1.positional 2.default 3.keyboard 4.ARBITRARY


def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(add(1))
