import time

# time.sleep(3)
# print("TIME'S UP!")


# example 2
# my_time = int(input("Enter the time in seconds: "))

# for x in range(0,  my_time):
#     print(x, end=" ")
#     time.sleep(1)
# print("\nTIMES'S UP!")

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    print(f"00:00:{seconds}")
    time.sleep(1)
