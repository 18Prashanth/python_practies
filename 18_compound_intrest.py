# python compound interest calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principal amount: "))
    if principle <= 0:
        print("pricipaol can't be less than or eqal to zero")
    else:
        break

while rate <= 0:
    rate = float(input("Enter the intrest rate: "))
    if rate <= 0:
        print("Intrest rate can't be less than or eqal to zero")
    else:
        break

while time <= 0:
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("Time can't be less than or eqal to zero")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"Balance sfter {time} yesr/s: ${total:.2f}")


# # python compound interest calculator

# principle = 0
# rate = 0
# time = 0

# while True:
#     principle = float(input("Enter the principal amount: "))
#     if principle <= 0:
#         print("pricipaol can't be less than or eqal to zero")
#     else:
#         break

# while True:
#     rate = float(input("Enter the intrest rate: "))
#     if rate <= 0:
#         print("Intrest rate can't be less than or eqal to zero")
#     else:
#         break

# while True:
#     time = float(input("Enter the time in years: "))
#     if time <= 0:
#         print("Time can't be less than or eqal to zero")
#     else:
#         break

# total = principle * pow((1 + rate / 100), time)
# print(f"Balance sfter {time} yesr/s: ${total:.2f}")
