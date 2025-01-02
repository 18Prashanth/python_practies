# name.len() = This function is used to get the length of the string
# name.find() = This function is used to find the string which is return first occurance
# name.rfind() = This function is used to find the string which is return last occurance
# name.capitalize() = This function is used to capitalize the first letter of the string


# name = input("Enter your full name: ")
phone_no = input("Enter the phone number: ")

# result = len(name)
# result = name.find("a")
# result = name.rfind("a")
# result = name.capitalize()
# result = name.upper()
# result = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = name.isalnum()
# result = phone_no.count("-")
result = phone_no.replace("-", "")

print(result)
