# Python writting files(.txt, .json, .csv)

# txt_data = "I Like pizza!"
import json
import csv
# employee = {
#     "name": "Spongebob",
#     "age": 30,
#     "job": "cook"
# }
employee = [["Name", "Age", "Job"],
            ["Prashanth", 23, "SDE"],
            ["Shivakumar", 50, "NGO"],
            ["Joo", 22, "Web developer"]]

employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

file_path = "C:/Users/Admin/OneDrive/Desktop/test/test3.csv"

try:
    # if we open a file 'with' its atuomatically close the file
    with open(file_path, "w", newline="") as file:
        # json.dump(employees, file, indent=4)
        writer = csv.writer(file)
        for row in employee:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exist")
