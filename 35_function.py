# function = A block of reusable code
# place () after the function name to invoke it

# example - 1
# def happy_birthday(name, age):
#     print(f"Happy birthday to {name}")
#     print(f"You are {age} years of old")
#     print("Happy birthday to you!")
#     print()


# happy_birthday("bro", 20)
# happy_birthday("smith", 24)
# happy_birthday("Joe", 20)

# example - 2
# def diaplay_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")

# diaplay_invoice("joeschmo", 100.01, "01/02")

# example - 3
# return = statement used to end a function
# and send a result back to the caller

# def add(x, y):
#     z = x + y
#     return z

# def diff(x, y):
#     z = x - y
#     return z

# def multiply(x, y):
#     z = x * y
#     return z

# def divide(x, y):
#     z = x / y
#     return z

# print(add(1, 2))
# print(diff(1, 2))
# print(multiply(1, 2))
# print(divide(1, 2))


# example - 4

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last


full_name = create_name("spongebob", "squarepants")

print(full_name)
