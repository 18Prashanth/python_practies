# 2dlist

# fruits = ["apple", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats = ["chicen", "fish", "turkey"]


groceries = [["apple", "orange", "banana", "coconut"],
             ["celery", "carrots", "potatoes"], ["chicen", "fish", "turkey"]]


for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
