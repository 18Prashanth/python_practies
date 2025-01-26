# Membership operators = used tp test whether a avlue or variable is found in a sequence
#                       (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in


# word = "APPLE"

# letter = input("Guess a letter in the secret word: ").upper()

# # if letter in word:
# #     print(f"There is a {letter}")
# # else:
# #     print(f"{letter} was not found")

# if letter not in word:
#     print(f"{letter} was not found")
# else:
#     print(f"There is a {letter}")


# example 2
# students = {"Prashanth", "Gowda", "Attahalli", "Shivakumar"}

# student = input("Enter the name of a student: ").capitalize()

# if student in students:
#     print(f"{student} is a student")
# else:
#     print(f"{student} was not found")


# if student not in students:
#     print(f"{student} was not found")
# else:
#     print(f"{student} is a student")


# example - 3

# grades = {"Prashanth": "A",
#           "Gowda": "B",
#           "Attahalli": "C",
#           "Shivakumar": "D"}

# student = input("Enter the name of a student: ").capitalize()


# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} was not found")

# example -
email = input("Enter a email!: ")

if "@" in email and "." in email:
    print("valid email")
else:
    print("Invalid Emanil")
