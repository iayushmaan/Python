# # QUE 1
num = int(input("enter ur no. :"))
if(num%2==0):
    print("ODD")
else:
    print("EVEN")


# # QUE 2
a = int(input("enter first no. :"))
b = int(input("enter second no. :"))
c = int(input("enter third no. :"))
if(a>=b and a>=c):
    print("first no. is largest:", a)
elif(b>=c):
    print("second no. is largest:", b)
else:
    print("third no. is largest:", c)


# # QUE 3
a = int(input("enter first no. :"))
b = int(input("enter second no. :"))
c = int(input("enter third no. :"))
d = int(input("enyer fourth no. :"))
if(a>=b and a>=c):
    print("first no. is largest:", a)
elif(b>=c):
    print("second no. is largest:", b)
elif(c>=d):
    print("third no. is largest:", c)
else:
    print("fourth no. is largest:", d)



# QUE 4
x = int(input("enter ur no.:"))
if(x%7==0):
    print("this no. is a multiple of 7")
else:
    print("this no. is not a multiple of 7 ")