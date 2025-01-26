# List Comprehension = A concise way to create list in python
#                      compact and easier to read than traditional looops
#                      [expression for value in itreable if condition]

# doubles = []
# for x in range(1, 11):
#     doubles.append(x * 2)

# print(doubles)


# example 2
doubles = [x * 2 for x in range(1, 11)]
print(doubles)
