# logial operators = evaluate multiple conditions (or, and not)
#                   or  = at least one condition must be true
#                   and = both condition must be True
#                   not = inverts the condition (not False, not True)


# temp = 35
# is_raining = False

# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancel")
# else:
#     print("The outdoor event is still scheduled")


# example

temp = 10
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT outside😁")
    print("It is sunny")
elif temp <= 0 and is_sunny:
    print("It is COLD outside")
    print("It is SUNNY")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside")
    print("It is SUNNY")
elif temp >= 28 and not is_sunny:
    print("It is HOT outside😁")
    print("It is CLOUDY")
elif temp <= 0 and not is_sunny:
    print("It is CLOUD outside")
    print("It is CLOUDY")
elif 28 > temp > 0 and not is_sunny:
    print("It is WARM outside")
    print("It is WARM")
