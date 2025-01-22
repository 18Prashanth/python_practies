# shopping cart program


foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy(Q to quit):")
    if food.lower() == 'q':
        break
    else:
        price = input(f"Enter the price of a {food}: $")
        foods.append(food)
        prices.append(price)
print(foods)
