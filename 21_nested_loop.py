# nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:

# for x in range(0, 10):
#     for y in range(0, 10):
#         for z in range(0, 10):
#             print(f"( {x}, {y}, {z})", end="")


# for x in range(1, 10):
#     print(x, end="")


# for x in range(3):
#     for y in range(1, 10):
#         print(y, end="")
#     print()


rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()
