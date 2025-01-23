# dictionar = a collection of {key:value} pairs
# ordred and changeable. No dupliactes

capitals = {"USA": "washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}
# print(dir(capitals))
# print(help(capitals))
country = input("Enter the country to know the Capitals: ")

print(capitals.get(country.capitalize()))
# print(capitals.values())
