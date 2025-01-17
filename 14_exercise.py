# validate user input exercise
# 1. username is no more than 12 character
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter the user name: ")

if len(username) > 12:
    print("Your user name can't be more than 12 character")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain number")
else:
    print(f"Welcome {username}!")
