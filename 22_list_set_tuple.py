# collection = single "variable" used to store multiple value
# List = [] ordered and changeable. Duplocated OK
# set = {} unordered and immutable, but Add/Remove ok, No duplicates
# Tuple= () ordered and unchangeable. Duplicates ok. Faster

# collection

# fruit = "apple"
# print(fruit)

# list

fruits = ["appple", "orange", "banana", "coconut"]
# print(fruits)
# print(fruits[0])
# print(fruits[1:])

# print(dir(fruits))

print(len(fruits))
print("ap" in fruits)

# fruits[0] = "pinapple"
# fruits.append("apple")
# fruits.remove("apple")
# fruits.insert(4, "pinapple")
# fruits.sort()
fruits.reverse()

for x in fruits:
    print(x)
