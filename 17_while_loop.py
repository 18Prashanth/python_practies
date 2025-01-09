# while loop = execute some code  WHILE some conditions remains true

name = input("Enter your name: ")

while name == "":
    print("You didi not enter your name")
    name = input("Enter your name: ")
print(f"Hello {name}")
