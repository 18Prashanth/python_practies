# keyword argument = an argument precede by an identifier
# helps with readability
# order of arguments doesn't matter
# 1. positional 2. default 3. KEYWORD 4. Arbitrary


# def hello(greeting, title, first, last):
#   print(f"{greeting} {title} {first} {last}")


# hello("Hello", title="Mr.", first="spongebob", last="squarepants")


# example - 2

# print("1", "2", "3", "4", sep="-")

# example - 3

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"


phone_num = get_phone(country=+91, area=974, first=740, last=4095)
print(phone_num)
