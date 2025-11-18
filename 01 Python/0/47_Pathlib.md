Here is an example of using Python's pathlib module for typical file system operations:

```python
from pathlib import Path

# Create a Path object for the current directory
p = Path('.')

# List all subdirectories
subdirs = [x for x in p.iterdir() if x.is_dir()]
print("Subdirectories:", subdirs)

# Create a new directory inside current directory
new_dir = p / "new_folder"
new_dir.mkdir(exist_ok=True)  # Creates the directory if it doesn't exist

# Create a Path object for a file inside the new directory
file_path = new_dir / "example.txt"

# Write text to the file
file_path.write_text("Hello, pathlib!\n", encoding='utf-8')

# Read the text back from the file
content = file_path.read_text(encoding='utf-8')
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
```

This example demonstrates creating directories, writing to and reading from files, checking file existence, renaming files,
and deleting files—all using pathlib's intuitive, object-oriented Path API. It works consistently across different operating
systems and is recommended over the older os.path module for path manipulations.[1][2][4]

[1](https://docs.python.org/3/library/pathlib.html)
[2](https://www.datacamp.com/tutorial/comprehensive-tutorial-on-using-pathlib-in-python-for-file-system-manipulation)
[3](https://switowski.com/blog/pathlib/) [4](https://realpython.com/python-pathlib/)
[5](https://www.geeksforgeeks.org/python/pathlib-module-in-python/)
[6](https://www.freecodecamp.org/news/how-to-use-pathlib-module-in-python/) [7](https://www.youtube.com/watch?v=yxa-DJuuTBI)
[8](https://www.spsanderson.com/steveondata/posts/2025-07-23/)
[9](https://www.pythoncheatsheet.org/cheatsheet/file-directory-path) [10](https://www.youtube.com/watch?v=P5rlLlztkNs)
