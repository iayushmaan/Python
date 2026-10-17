x = int(input("Enter First no. : "))
y = int(input("Enter Second no. : "))

operator = input("Enter Operator : ")

if(operator == "+"):
    print(x + y)
elif(operator == "-"):
    print(x - y)
elif(operator == "*"):
    print(x * y)
elif(operator == "/"):
    if(y == 0):
        print("Cannot perform operation with zero!")
    else:
        print(x / y)
elif(operator == "**"):
    print(x ** y)
elif(operator == "//"):
    if(y == 0):
        print("Cannot perform operation with zero!")
    else:
        print(x // y)
elif(operator == "%"):
    if(y == 0):
        print("Cannot perform operation with zero!")
    else:
        print(x % y)
else:
    print("Invalid operator! Please use a valid operator.")