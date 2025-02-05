# python reading files (.txt, .json, .csv)

import json

file_path = "C:/Users/Admin/OneDrive/Desktop/test/test2.json"

try:
    with open(file_path, "r") as file:
        # content = file.read()
        content = json.load(file)
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("you do not have permission to read that files")
