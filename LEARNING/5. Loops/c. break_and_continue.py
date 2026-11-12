# BREAK STATEMENT
# The break statement is used to terminate a loop immediately when a specified condition is met.

# CONTINUE STATEMENT
# The continue(skip) statement skips the current iteration and moves to the next iteration of the loop.


# BREAK

#1
i = 1
while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1
print("end")


#2
num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36
i = 0
while i < len(num):
    if num[i] == x:
       print("FOUND at idx : ", i)
       break
    else:
        print("finding...")
    i += 1






# CONTINUE

#1
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue #skip
    print(i)
    i += 1


#2 (even)
i = 1
while i <= 10:
    if i%2 == 0:
        i += 1
        continue #skip
    print(i)
    i += 1


#3 (odd)
i = 1
while i <= 10:
    if i%2 != 0:
        i += 1
        continue
    print (i)
    i += 1