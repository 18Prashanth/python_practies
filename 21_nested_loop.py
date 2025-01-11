# nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:

for x in range(0, 10):
    for y in range(0, 10):
        for z in range(0, 10):
            print(f"( {x}, {y}, {z})", end="")
