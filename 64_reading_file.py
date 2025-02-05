# python reading files (.txt, .json, .csv)

import json
import csv

file_path = "C:/Users/Admin/OneDrive/Desktop/test/test3.csv"

try:
    with open(file_path, "r") as file:
        # content = file.read()
        # content = json.load(file)
        content = csv.reader(file)
        for line in content:
            print(line)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("you do not have permission to read that files")
