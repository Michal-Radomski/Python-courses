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
