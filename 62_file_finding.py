# Python file detection

import os

file_path = "C:/Users/Admin/OneDrive/Desktop/test"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That location doesn't exist")
