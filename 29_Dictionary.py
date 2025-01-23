# dictionar = a collection of {key:value} pairs
# ordred and changeable. No dupliactes

capitals = {"USA": "washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}
# print(dir(capitals))
# print(help(capitals))
# country = input("Enter the country to know the Capitals: ")

# print(capitals.get(country.capitalize()))
# print(capitals.values())
# print(capitals.get("USA"))

# capitals.update({"Germany": "Berlin"})
# capitals.pop("China")
# capitals.update({"USA": "Detroit"})
# capitals.popitem()
# capitals.clear()

# key = capitals.keys()
# for key in capitals.keys():
#     print(key)
# value = capitals.values()
# print(value)

for key, value in capitals.items():
    print(f"{key}: {value}")


# country = ""
# while True:
#     country = input(
#         "Enter the country to get to Know the capital city(q to quit): ")
#     if country.lower() == 'q':
#         break
#     else:
#         print(capitals.get(country.upper()))
