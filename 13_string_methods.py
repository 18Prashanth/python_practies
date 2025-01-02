# name.len() = This function is used to get the length of the string
# name.find() = This function is used to find the string which is return first occurance
# name.rfind() = This function is used to find the string which is return last occurance
# name.capitalize() = This function is used to capitalize the first letter of the string


name = input("Enter your full name: ")
phone_no = input("Enter the phone number: ")

result = len(name)
print(result)
result = name.find("a")
print(result)
result = name.rfind("a")
print(result)
result = name.capitalize()
print(result)
result = name.upper()
print(result)
result = name.lower()
print(result)
result = name.isdigit()
print(result)
result = name.isalpha()
print(result)
result = name.isalnum()
print(result)
result = phone_no.count("-")
print(result)
result = phone_no.replace("-", "")
print(result)

# print(help(str))
