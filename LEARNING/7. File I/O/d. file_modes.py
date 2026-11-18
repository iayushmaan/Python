# File Modes:
# r  - Opens a file for reading. The stream is positioned at the beginning.
# r+ - Opens a file for reading and writing. The stream is positioned at the beginning.
# w  - Opens a file for writing. Truncates existing content or creates a new file.
# w+ - Opens a file for reading and writing. Creates a file if it doesn't exist; otherwise, truncates it.
# a  - Opens a file for writing. Creates it if it doesn't exist and positions the stream at the end.
# a+ - Opens a file for reading and writing. Creates it if it doesn't exist and positions the stream at the end.

#Truncating means deleting the existing content of a file to make it empty.

# r+ - overwrite - pointer at starting - no truncation
# w+ - overwrite - pointer at starting - truncate
# a+ - Append - Pointer initially at the end - no truncation.
#       Writing always happens at the end of the file.




f = open("/Users/ayushmaan/Desktop/Python🐍/LEARNING/7. File I/O/sample1.txt", "r+")
f.write("macbook")
print(f.read())
f.close


f = open("/Users/ayushmaan/Desktop/Python🐍/LEARNING/7. File I/O/sample2.txt", "w+")
print(f.read())
f.write("Exact pricing will be provided by your card issuer, subject to your card issuer's terms and conditions")
f.close


f = open("/Users/ayushmaan/Desktop/Python🐍/LEARNING/7. File I/O/sample3.txt", "a+")
print(f.read())
f.write("The M5 chip isn't just an upgrade, it's a game changer, delivering phenomenal performance. Prepare for lift-off.")
f.close