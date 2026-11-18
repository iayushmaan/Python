# I. #File I/O in Python

# Python allows us to perform operations on files.
# We can read data from files and write data into files.

# Types of Files:

# 1. Text Files:
# Store data in a human-readable format.
# Examples: .txt, .docx, .log

# 2. Binary Files:
# Store data in binary format (0s and 1s).
# Examples: .mp4, .mov, .png, .jpeg




# II. #Opening, Reading & Closing a File

# We must open a file before performing read or write operations.

# Syntax:
# f = open("file_name", "mode")

# file_name: Name of the file (e.g., sample.txt, demo.docx)
# mode: Specifies the purpose of opening the file.

# File Modes:
# "r" = Read mode (used to read an existing file).
# "w" = Write mode (used to write data into a file).

# Reading a file:
# data = f.read()
# read() returns the contents of the file.

# Closing a file:
# f.close()
# close() closes the file and releases its resources.






# III #File Opening Modes in Python

# 'r' = Read mode (default mode).
# Opens a file for reading data.

# 'w' = Write mode.
# Opens a file for writing and truncates existing content.
# Creates a new file if it does not exist.

# 'x' = Exclusive creation mode.
# Creates a new file for writing.
# Gives an error if the file already exists.

# 'a' = Append mode.
# Adds new data at the end of the file.
# Creates a new file if it does not exist.

# 'b' = Binary mode.
# Used to read or write binary files.

# 't' = Text mode (default mode).
# Used to read or write text files.

# '+' = Update mode.
# Opens a file for both reading and writing.




#Important combinations:

# 'rb' = Read binary
# 'wb' = Write binary
# 'r+' = Read and write
# 'w+' = Write and read (truncates existing content)
# 'a+' = Append and read




#Truncate → To remove existing content from a file.
#Append → To add new content at the end of existing content.
#Overwrite → To replace existing content with new content.



f = open("/Users/ayushmaan/Desktop/Python🐍/LEARNING/7. File I/O/sample.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()



f = open("/Users/ayushmaan/Desktop/Python🐍/LEARNING/7. File I/O/sample.txt", "r")
data = f.read(8)
print(data)
print(type(data))
f.close()