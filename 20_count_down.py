import time

# time.sleep(3)

# print("TIME'S UP!")

my_time = int(input("Enter the time in seconds: "))

for x in range(0,  my_time):
    print(x, end=" ")
    time.sleep(1)
print("\nTIMES'S UP!")
