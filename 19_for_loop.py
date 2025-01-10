# for loops = execute a block of code a fixed number of ti,es.
#           you can iterate over a range, string, sequence, etc.
# for "variable" in range(start, end, difference)   start=0, end=end-1


# for x in range(1, 10):
#     print(x)


# for x in reversed(range(1, 10, 2)):
#     print(x)
# print("HAPPY NEW YEAR!")


# credit_card = "1234-5678-9012-3456"
# for x in credit_card:
#     print(x)

for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x, end=" ")
