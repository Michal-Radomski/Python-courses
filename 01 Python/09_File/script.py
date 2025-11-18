# -*- coding: utf-8 -*-
from pathlib import Path

my_file = open("test.txt")
print(my_file)  # <_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>
print(my_file.read())

print(
    my_file.read()
)  # it won't be printing anything. because the cursor is at the end of the file.

print("Seek 0")
my_file.seek(0)  # we reset the cursor to the initial position.

print(
    my_file.read()
)  # and so we can now read the file from the initial position till end.

print("Seek 0")
my_file.seek(0)

print(my_file.readline())  # reads a line and stop the cursor
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())

print("Seek 0")
my_file.seek(0)

print(my_file.readlines())  # store all the lines in a list
print(my_file.readlines())

my_file.close()


with open("test.txt", mode="a") as my_file:
    text = my_file.write("I am HAPPY!")
    print(text)  # it prints the no. of letters written into the file


with open("test.txt", mode="r") as my_file:
    print(my_file.read())

"""
mode = 'w' : it creates a new file and write into it. If there is an exiting file with the same name, it replaces it.
mode = 'r' : it is used to read the file
mode = 'r+' : it is used to read and write into the file. but it writes from position 0, which might replace some existing text.
mode = 'a' : it appends to the existing file. meaning writing to the file keeping the old content intact.
             if the file doesn't exist, it creates a new one.

if we don't mention the mode, by default it will be considered 'r' mode.

with 'with' we don't need to close the file manually.
"""

with open("./example/example.txt", mode="r") as my_file:
    print(my_file.read())

# Create a Path object for the current directory
p = Path(".")

# List all subdirectories
subdirs = [x for x in p.iterdir() if x.is_dir()]
print("Subdirectories:", subdirs)

# Create a new directory inside current directory
new_dir = p / "new_folder"
new_dir.mkdir(exist_ok=True)  # Creates the directory if it doesn't exist

# Create a Path object for a file inside the new directory
file_path = new_dir / "example.txt"

# Write text to the file
file_path.write_text("Hello, pathlib!\n", encoding="utf-8")

# Read the text back from the file
content = file_path.read_text(encoding="utf-8")
print("File content:", content)

# Check if the file exists
print("File exists?", file_path.exists())

# Rename or move the file (to 'renamed.txt' in the same directory)
renamed_path = new_dir / "renamed.txt"
file_path.rename(renamed_path)
print("Renamed file path:", renamed_path)

# Delete the renamed file
renamed_path.unlink()
print("File deleted.")

# Optional: Remove the created directory (only if empty)
new_dir.rmdir()
