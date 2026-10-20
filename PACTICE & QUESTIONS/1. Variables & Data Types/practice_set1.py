#QUE 1
x = input("enter your name : ")
y = int(input("enter your age : "))
print(x , y)


#QUE 2
x = int(input("enter 1st no. : "))
y = int(input("enter 2nd no. : "))
print(x + y)
print(x - y)
print(x * y)
print(x / y)



#QUE 3
a = 20
b = 40
a , b = b , a
print(a)
print(b)




#QUE 4
x = int(input("enter a no. : "))
a = (x)%10
print(a)



#QUE 5
x = int(input("enter 1st no. : "))
y = int(input("enter 2nd no. : "))
z = int(input("enter 3rd no. : "))
avg = (x + y + z)/3
print("average :", avg)




#QUE 6
x = int(input("enter total seconds : "))
minutes = x // 60 
seconds = x % 60
print(minutes, "minutes" , seconds, "seconds")




#QUE 7
a = 10
b = 20
c = 30

a, b, c = b, c, a
print("a :", a)
print("b :", b)
print("c :", c)



#QUE 8
x = int(input("enter a no. : "))
a = (x)%10
b = (x)//10
print("Tens digit: " ,b)
print("Once digit: " ,a)




#QUE 9
price = int(input("enter price of the product : "))
quantity = int(input("enter quantity of that item : "))
total_bill = (price * quantity)
print("total bill : "  ,total_bill)




#QUE 10
subj1 = int(input("Enter marks 1 : "))
subj2 = int(input("Enter marks 2 : "))
subj3 = int(input("Enter marks 3 : "))
subj4 = int(input("Enter marks 4 : "))
subj5 = int(input("Enter marks 5 : "))

a = (subj1 + subj2 + subj3 + subj4 + subj5)
b = ((subj1 + subj2 + subj3 + subj4 + subj5)/500) * 100
print( "total marks : ",a)
print( "percentage : ",b)