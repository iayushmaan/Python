with open("/Users/ayushmaan/Desktop/Python🐍/LEARNING/7. File I/O/sample1.txt", "r") as f:
    data = f.read()
    print(data)


with open ("/Users/ayushmaan/Desktop/Python🐍/LEARNING/7. File I/O/sample1.txt", "w") as f:
    f.write("python")