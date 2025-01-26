# if __name__=='__main__': (this script can be impoerted OR run standalone)
#                         function and classes in this module can be reused
#                         without the main block of code executing


def favorite_food(food):
    print(f"Your favorite food is {food}")


def main():
    print("This is script1")
    favorite_food("pizza")
    print("Goodbye!")


if __name__ == '__main__':
    main()
