# dictionar = a collection of {key:value} pairs
# ordred and changeable. No dupliactes

capitals = {"USA": "washington D.C.",
            "INDIA": "New Delhi",
            "CHINA": "Beijing",
            "RUSSIA": "Moscow"}
# print(dir(capitals))
# print(help(capitals))
# country = input("Enter the country to know the Capitals: ")

# print(capitals.get(country.capitalize()))
# print(capitals.values())
country = ""

while True:
    country = input(
        "Enter the country to get to Know the capital city(q to quit): ")
    if country.lower() == 'q':
        break
    else:
        print(capitals.get(country.upper()))
