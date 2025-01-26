# List Comprehension = A concise way to create list in python
#                      compact and easier to read than traditional looops
#                      [expression for value in itreable if condition]

# doubles = []
# for x in range(1, 11):
#     doubles.append(x * 2)

# print(doubles)


# example 2
# doubles = [x * 2 for x in range(1, 11)]
# triples = [y * 3 for y in range(1, 11)]
# squares = [z * 3 for z in range(1, 11)]

# print(squares)

# fruits = ["apple", "orange", "banana"]
# fruit_chars = [fruit[0] for fruit in fruits]

# print(fruit_chars)


# example ---

numbers = [1, -2, -3, -4, -5, -6]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
print(even_nums)
