# QUE 1
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for num in list:
    print (num)


# QUE 2
list = (1, 4, 25, 9, 16, 25, 36, 49, 64, 81, 25, 100)
x = 25
idx = 0
for el in list:
    if el == x:
        print("number founded at : ", idx)
    idx += 1


# QUE 3
list = (1, 4, 25, 9, 16, 25, 36, 49, 64, 81, 25, 100)
x = 25
idx = 0
for el in list:
    if el == x:
        print("founded at", idx)
        break
    idx += 1