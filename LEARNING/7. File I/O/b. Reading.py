# Reading a File in Python

# read():
# Reads the entire content of the file at once.
# data = f.read()

# readline():
# Reads one line at a time from the file.
# data = f.readline()




# --->
f = open("/Users/ayushmaan/Desktop/Python🐍/LEARNING/7. File I/O/sample.txt", "r")

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

f.close()




# --->
f = open("/Users/ayushmaan/Desktop/Python🐍/LEARNING/7. File I/O/sample.txt", "r")

read = f.read()
print(read)

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

# If read() is executed first, readline() will not work afterward
# because read() reads the entire file and moves the file pointer to the end.