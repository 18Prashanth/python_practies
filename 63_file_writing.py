# Python writting files(.txt, .json, .csv)

txt_data = "I Like pizza"

file_path = "C:/Users/Admin/OneDrive/Desktop/test/test.txt"

try:
    with open(file_path, "x") as file:  # if we open a file 'with' its atuomatically close the file
        file.write(txt_data)
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("File already exist")
