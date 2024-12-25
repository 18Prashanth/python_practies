# if = Do some code only if  some condition is True Else do something else

age = int(input("Enter your Age: "))

if age >= 18:
    print(" You are noe signed up!")
elif age < 0:
    print("You haven't born yet!")
else:
    print("You must be 18+ to sign up!")
