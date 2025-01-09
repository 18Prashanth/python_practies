# format specifiers = {value:flags} format a value based on what
#  flags are inserted

price1 = 3000.14159
price2 = -9870.65
price3 = 12000.34

# print(f"Price 1 is ${price1:.1f}")
# print(f"Price 2 is ${price2:.1f}")
# print(f"Price 3 is ${price3:.1f}")

# print(f"Price 1 is ${price1: 10}")
# print(f"Price 2 is ${price2: 10}")
# print(f"Price 3 is ${price3: 10}")


# print(f"Price 1 is ${price1: 010}")
# print(f"Price 2 is ${price2: 010}")
# print(f"Price 3 is ${price3: 010}")

# print(f"Price 1 is ${price1: <10}")
# print(f"Price 2 is ${price2: <10}")
# print(f"Price 3 is ${price3: <10}")


# print(f"Price 1 is ${price1: ^10}")
# print(f"Price 2 is ${price2: ^10}")
# print(f"Price 3 is ${price3: ^10}")

print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")
