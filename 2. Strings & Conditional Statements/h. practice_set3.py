num = int(input("enter the no. : "))
if(num>=0) and (num<=9):
    print("one digit")
elif(num>=10) and (num<=99):
    print("two digit")
elif(num>=100) and (num<=999):
    print("three digit")
elif(num>=1000) and (num<=9999):
    print("four digit")
else:
    print("not defined")