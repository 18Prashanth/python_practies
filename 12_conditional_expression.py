# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                         Print or assign one of two values based on a condition
#                         X if condition else Y


num = 5
a = 6
b = 7
age = 13
temperature = 30
user_role = "Admin"


print("Positive" if num > 0 else "Negative")
result = "EVEN" if num % 2 == 0 else "ODD"
max_num = a if a > b else b
min_num = a if a < b else b
status = "ADULT" if age >= 18 else "CHILD"
wheather = "HOT" if temperature > 20 else "COLD"
access_level = "Full Access" if user_role == "Admin" else "Limited Access"


print(f"The maximum number is: {max_num} ")
print(f"The minimum number is: {min_num} ")
print(status)
print(wheather)
print(access_level)
