# default argument = A default value for certain parameters
#                   default is used when that argument is Omitted
#                   make your fuunctions more flexible, reducces # of argumnets
#                    1. positional, 2. DEFAULT, 3. Keyword, 4. ARbitrary

# example 1
# def net_price(list_price, discount=0, tax=0.05):
#     return list_price * (1 - discount) * (1 + tax)

# print(net_price(500))
# print(net_price(500, 0.1, 0))

# example 2
import time


def count(start, end):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")


count(0, 10)
