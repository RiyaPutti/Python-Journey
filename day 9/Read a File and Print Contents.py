with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
# The code opens a file named "sample.txt" in read mode and prints its contents to the console.
# The file is automatically closed after the block of code is executed.
# The 'with' statement ensures that the file is properly closed after its suite finishes, even if an exception is raised.
# This is a good practice to avoid file leaks and ensure that resources are managed properly.
# The 'r' mode is used to open the file for reading. If the file does not exist, a FileNotFoundError will be raised.
# The 'read' method reads the entire content of the file into a string. 
# If the file is large, consider using 'readline' or 'readlines' to read it line by line or into a list of lines.

# The 'print' function outputs the content to the console.
# If you want to read the file line by line, you can use a loop:
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())  # 'strip()' removes leading and trailing whitespace, including newlines.
        
# This method is more memory efficient for large files, as it reads one line at a time.
# You can also use 'readlines' to read all lines into a list:
with open("sample.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())
# This reads all lines into a list and then iterates over the list to print each line.
# If you want to handle exceptions, you can use a try-except block:
try: 
    with open("sample.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file was not found.")
# This will catch the FileNotFoundError and print a message instead of crashing the program.

# You can also specify the encoding when opening a file, which is useful for text files with special characters:
with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

        
# This specifies that the file should be read using UTF-8 encoding, which is a common encoding for text files.
# If you want to write to a file instead of reading, you can use the 'w' mode:  
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.")
    
# This will create a new file named "output.txt" and write the specified text to it.
# If the file already exists, it will be overwritten.
# If you want to append to a file instead of overwriting it, you can use the 'a' mode:
with open("output.txt", "a") as file:
    file.write("\nThis line is appended.")
# This will add the specified text to the end of the file without deleting the existing content.
# You can also use the 'x' mode to create a new file, which will raise an error if the file already exists:
with open("newfile.txt", "x") as file:
    file.write("This is a new file.")
# This will create a new file named "newfile.txt" and write the specified text to it.
# If the file already exists, a FileExistsError will be raised.
# In summary, the 'with' statement is a good practice for file handling in Python, as it ensures that files are properly closed after their use.
# The 'r', 'w', 'a', and 'x' modes allow you to read, write, append, and create files, respectively.
# Always handle exceptions when dealing with file operations to avoid crashes and ensure that your program can handle errors gracefully.
# This is a simple example of reading a file and printing its contents.
# You can also use the 'read' method with a size argument to read a specific number of bytes:
with open("sample.txt", "r") as file:
    content = file.read(10)  # Reads the first 10 bytes of the file
    print(content)
# This can be useful if you only want to read a portion of the file.
# You can also use the 'tell' method to get the current position of the file pointer:
with open("sample.txt", "r") as file:
    print(file.tell())  # Prints the current position of the file pointer (0 at the beginning)
    content = file.read(10)  # Reads the first 10 bytes of the file
    print(content)
    print(file.tell())  # Prints the new position of the file pointer (10 after reading 10 bytes)
# The 'tell' method returns the current position of the file pointer in bytes.
# You can also use the 'seek' method to move the file pointer to a specific position:
with open("sample.txt", "r") as file:
    file.seek(5)  # Moves the file pointer to the 5th byte
    content = file.read(10)  # Reads the next 10 bytes from the new position
    print(content)
# The 'seek' method allows you to move the file pointer to a specific position in the file.
# You can also use negative offsets to move the pointer from the end of the file:
with open("sample.txt", "r") as file:
    file.seek(-10, 2)  # Moves the file pointer 10 bytes from the end of the file
    content = file.read(10)  # Reads the next 10 bytes from the new position
    print(content)
# This can be useful for reading the last few bytes of a file.
# You can also use the 'truncate' method to resize the file:
with open("sample.txt", "r+") as file:
    file.truncate(10)  # Resizes the file to 10 bytes
    content = file.read()  # Reads the remaining content of the file
    print(content)
# The 'truncate' method resizes the file to the specified size. If the file is larger than the specified size, the excess content is removed.
# If the file is smaller than the specified size, it is padded with null bytes.
# You can also use the 'flush' method to flush the internal buffer to the file:
with open("sample.txt", "r+") as file:
    file.write("Hello, World!")  # Writes to the file
    file.flush()  # Flushes the internal buffer to the file
    content = file.read()  # Reads the remaining content of the file
    print(content)
# The 'flush' method flushes the internal buffer to the file, ensuring that all data is written to the file.
# This can be useful if you want to ensure that all data is written to the file before performing other operations.
# You can also use the 'os' module to perform file operations:
import os
# Check if a file exists
if os.path.exists("sample.txt"):
    print("File exists.")
else:
    print("File does not exist.")
# Get the size of a file
file_size = os.path.getsize("sample.txt")
print(f"File size: {file_size} bytes")
# Delete a file
os.remove("sample.txt")

# This will delete the file named "sample.txt". Be careful when using this operation, as it cannot be undone.
# You can also use the 'shutil' module to perform file operations:
import shutil
# Copy a file
shutil.copy("sample.txt", "copy_sample.txt")  # Copies the file to a new location
# Move a file
shutil.move("sample.txt", "new_location/sample.txt")  # Moves the file to a new location
# This will move the file to the specified location. If the destination directory does not exist, a FileNotFoundError will be raised.
# You can also use the 'glob' module to find files matching a specific pattern:
import glob
# Find all text files in the current directory
text_files = glob.glob("*.txt")
print(text_files)
# This will return a list of all text files in the current directory.
# You can also use the 'fnmatch' module to match filenames using Unix shell-style wildcards:
import fnmatch
# Find all text files in the current directory
text_files = fnmatch.filter(os.listdir("."), "*.txt")
print(text_files)
# This will return a list of all text files in the current directory.
# You can also use the 'pathlib' module to perform file operations:
from pathlib import Path
# Create a Path object

path = Path("sample.txt")
# Check if the file exists
if path.exists():
    print("File exists.")
else:
    print("File does not exist.")
# Get the size of the file
file_size = path.stat().st_size
print(f"File size: {file_size} bytes")
# Read the contents of the file
with path.open("r") as file:
    content = file.read()
    print(content)
# Write to the file
with path.open("w") as file:
    file.write("Hello, World!")
# This will create a new file named "sample.txt" and write the specified text to it.
# If the file already exists, it will be overwritten.
# You can also use the 'rename' method to rename a file:
path.rename("new_sample.txt")  # Renames the file to "new_sample.txt"
# This will rename the file to the specified name. If the new name already exists, a FileExistsError will be raised.
# You can also use the 'unlink' method to delete a file:
path.unlink()  # Deletes the file
# This will delete the file. Be careful when using this operation, as it cannot be undone.
# You can also use the 'mkdir' method to create a new directory:
path.mkdir(parents=True, exist_ok=True)  # Creates a new directory
# This will create a new directory. If the directory already exists, a FileExistsError will be raised.
# You can also use the 'rmdir' method to remove a directory:
path.rmdir()  # Removes the directory
# This will remove the directory. Be careful when using this operation, as it cannot be undone.
# You can also use the 'shutil' module to perform directory operations:
import shutil
# Copy a directory
shutil.copytree("source_directory", "destination_directory")  # Copies the directory to a new location
# Move a directory
shutil.move("source_directory", "new_location/source_directory")  # Moves the directory to a new location
# This will move the directory to the specified location. If the destination directory does not exist, a FileNotFoundError will be raised.
# You can also use the 'os' module to perform directory operations:
import os
# List all files and directories in the current directory
files_and_directories = os.listdir(".")
print(files_and_directories)
# This will return a list of all files and directories in the current directory.
# You can also use the 'os.walk' method to recursively list all files and directories in a directory:
for root, dirs, files in os.walk("."):
    print(f"Root: {root}")
    print(f"Directories: {dirs}")
    print(f"Files: {files}")
# This will recursively list all files and directories in the specified directory.
# You can also use the 'os.path' module to perform path operations:
import os.path
# Join two paths
path1 = "directory"
path2 = "file.txt"
joined_path = os.path.join(path1, path2)
print(joined_path)  # Prints "directory/file.txt" on Unix-like systems and "directory\file.txt" on Windows
# This will join the two paths using the appropriate separator for the operating system.
# You can also use the 'os.path.abspath' method to get the absolute path of a file:
absolute_path = os.path.abspath("file.txt")
print(absolute_path)  # Prints the absolute path of the file
# This will return the absolute path of the specified file.
# You can also use the 'os.path.basename' method to get the base name of a file:
base_name = os.path.basename("directory/file.txt")
print(base_name)  # Prints "file.txt"
# This will return the base name of the specified file.
# You can also use the 'os.path.dirname' method to get the directory name of a file:
directory_name = os.path.dirname("directory/file.txt")
print(directory_name)  # Prints "directory"
# This will return the directory name of the specified file.
# You can also use the 'os.path.splitext' method to split a file name into its base name and extension:
base_name, extension = os.path.splitext("file.txt")
print(base_name)  # Prints "file"
print(extension)  # Prints ".txt"
# This will return the base name and extension of the specified file.
# You can also use the 'os.path.exists' method to check if a file or directory exists:
exists = os.path.exists("file.txt")
print(exists)  # Prints True if the file or directory exists, False otherwise
# This will return True if the specified file or directory exists, and False otherwise.
# You can also use the 'os.path.isfile' method to check if a path is a file:

is_file = os.path.isfile("file.txt")
print(is_file)  # Prints True if the path is a file, False otherwise
# This will return True if the specified path is a file, and False otherwise.
# You can also use the 'os.path.isdir' method to check if a path is a directory:
is_directory = os.path.isdir("directory")
print(is_directory)  # Prints True if the path is a directory, False otherwise
# This will return True if the specified path is a directory, and False otherwise.
# You can also use the 'os.path.getsize' method to get the size of a file:
file_size = os.path.getsize("file.txt")
print(file_size)  # Prints the size of the file in bytes

# This will return the size of the specified file in bytes.
# You can also use the 'os.path.getmtime' method to get the last modification time of a file:
modification_time = os.path.getmtime("file.txt")
print(modification_time)  # Prints the last modification time of the file in seconds since the epoch
# This will return the last modification time of the specified file in seconds since the epoch.
# You can also use the 'os.path.getatime' method to get the last access time of a file:
access_time = os.path.getatime("file.txt")
print(access_time)  # Prints the last access time of the file in seconds since the epoch
# This will return the last access time of the specified file in seconds since the epoch.
# You can also use the 'os.path.getctime' method to get the creation time of a file:
creation_time = os.path.getctime("file.txt")
print(creation_time)  # Prints the creation time of the file in seconds since the epoch
# This will return the creation time of the specified file in seconds since the epoch.
# You can also use the 'os.path.samefile' method to check if two paths refer to the same file:
same_file = os.path.samefile("file1.txt", "file2.txt")
print(same_file)  # Prints True if the two paths refer to the same file, False otherwise
# This will return True if the two specified paths refer to the same file, and False otherwise.
# You can also use the 'os.path.realpath' method to get the canonical path of a file:
real_path = os.path.realpath("file.txt")
print(real_path)  # Prints the canonical path of the file

# This will return the canonical path of the specified file, resolving any symbolic links.
# You can also use the 'os.path.normpath' method to normalize a path:
normalized_path = os.path.normpath("directory/../file.txt")
print(normalized_path)  # Prints the normalized path of the file
# This will return the normalized path of the specified file, resolving any redundant separators and up-level references.
# You can also use the 'os.path.expanduser' method to expand a user directory:
expanded_path = os.path.expanduser("~/file.txt")
print(expanded_path)  # Prints the expanded path of the file
# This will return the expanded path of the specified file, replacing the user directory with the full path.
# You can also use the 'os.path.expandvars' method to expand environment variables:
expanded_path = os.path.expandvars("$HOME/file.txt")
print(expanded_path)  # Prints the expanded path of the file
# This will return the expanded path of the specified file, replacing environment variables with their values.
# You can also use the 'os.path.abspath' method to get the absolute path of a file:
absolute_path = os.path.abspath("file.txt")
print(absolute_path)  # Prints the absolute path of the file
# This will return the absolute path of the specified file.
# You can also use the 'os.path.relpath' method to get the relative path of a file:
relative_path = os.path.relpath("file.txt", "directory")
print(relative_path)  # Prints the relative path of the file
# This will return the relative path of the specified file with respect to the specified directory.
# You can also use the 'os.path.commonpath' method to get the common path prefix of a list of paths:
common_path = os.path.commonpath(["directory/file1.txt", "directory/file2.txt"])
print(common_path)  # Prints the common path prefix of the list of paths
# This will return the common path prefix of the specified list of paths.
# You can also use the 'os.path.commonprefix' method to get the common prefix of a list of paths:
common_prefix = os.path.commonprefix(["directory/file1.txt", "directory/file2.txt"])
print(common_prefix)  # Prints the common prefix of the list of paths
# This will return the common prefix of the specified list of paths.

# You can also use the 'os.path.split' method to split a path into its directory and base name:
directory, base_name = os.path.split("directory/file.txt")
print(directory)  # Prints the directory name
print(base_name)  # Prints the base name of the file
# This will return the directory name and base name of the specified file.

# You can also use the 'os.path.splitdrive' method to split a path into its drive and path:
drive, path = os.path.splitdrive("C:/directory/file.txt")
print(drive)  # Prints the drive name
print(path)  # Prints the path of the file
# This will return the drive name and path of the specified file.

# You can also use the 'os.path.splitext' method to split a path into its base name and extension:
base_name, extension = os.path.splitext("directory/file.txt")
print(base_name)  # Prints the base name of the file
print(extension)  # Prints the extension of the file
# This will return the base name and extension of the specified file.



