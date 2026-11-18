# QUE 1
with open("/Users/ayushmaan/Desktop/Python🐍/LEARNING/7. File I/O/practice.txt", "w") as f:
    f.write("Hi everyone \nwe are learning File I/O \nusing Java \nI like programming in Java")


# QUE 2
with open("/Users/ayushmaan/Desktop/Python🐍/LEARNING/7. File I/O/practice.txt","r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)

with open("/Users/ayushmaan/Desktop/Python🐍/LEARNING/7. File I/O/practice.txt","w") as f:
    f.write(new_data)


# QUE 3
def check_for_word():
    word = "learning"
    with open("/Users/ayushmaan/Desktop/Python🐍/LEARNING/7. File I/O/practice.txt","r") as f:
        data = f.read()
        if word in data:
            print("FOUND")
        else:
            print("NOT FOUND")

check_for_word()



# QUE 4
def check_for_line():
    word = "learning"
    data = True
    line_number = 1
    with open("/Users/ayushmaan/Desktop/Python🐍/LEARNING/7. File I/O/practice.txt", "r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(line_number)
                return
            line_number += 1
    return -1

check_for_line()



# QUE 5
count = 0
with open("/Users/ayushmaan/Desktop/Python🐍/LEARNING/7. File I/O/practice1.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if int(val) % 2 == 0: #even no.
            count += 1
print(count)