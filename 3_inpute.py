# # inpute = the function that prompts the user to enter data
# # the function return the enter data as a string

# first_name = input("what is your name?: ")
# Age = input(" How old are you? :")
# # print(type(first_name))
# print(f"Hello, {first_name}!")
# print(f"you are, {Age} years old")


# Program to calculate the area of rectangle

# length = int(input(" Enter the length of rectangle: "))
# width = int(input(" Enter the width of rectangle: "))
# Area = length * width
# # print(f"The area of rectangle is {Area} cm")
# print(Area)


item = input("What item would you like to buy?: ")
price = float(input("what is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"you have bought {quantity} x {item} /s")
print(f" your total is: ${total}")
