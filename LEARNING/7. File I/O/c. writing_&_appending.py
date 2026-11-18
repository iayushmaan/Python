# Writing to a File

# Open a file in write mode ("w").
# Write mode overwrites the entire file if it already exists.

# Use the write() method to write content into the file.
# Example: f.write("this is a new line")

# Open a file in append mode ("a").
# Append mode adds new content at the end of the existing file.

# Use the write() method to add content without overwriting existing data.
# Example: f.write("this is a new line")




#1
#--->
f = open("/Users/ayushmaan/Desktop/Python🐍/LEARNING/7. File I/O/sample.txt", "w")

f.write("Just a guy learning Python and figuring things out.")

f.close()




#--->
f = open("/Users/ayushmaan/Desktop/Python🐍/LEARNING/7. File I/O/sample.txt", "a")

f.write("\nPython")

f.close()





#2
# If we use "w" (write) or "a" (append) mode to open a file that does not exist, Python automatically creates the file.
#--->
f = open("/Users/ayushmaan/Desktop/Python🐍/LEARNING/7. File I/O/sample1.txt", "w")

f.write("Hello")

f.close()


#--->
f = open("/Users/ayushmaan/Desktop/Python🐍/LEARNING/7. File I/O/sample2.txt", "w")

f.write("new txt file")

f.close()