# QUE 1
x = int(input("enter a no. : "))
if x % 2 == 0:
    print("EVEN")
else:
    print("ODD")



# QUE 2
x = int(input("enter a no. : "))
if x>0 :
    print("Positive no.")
elif x<0 :
    print("Negative no.")
else:
    print("Zero")




# QUE 3
x = int(input("enter 1st no. : "))
y = int(input("enter 2nd no. : "))

if x > y :
    print(x ,"is greater")
elif x < y :
    print(y, "is greater")
else:
    print("Both are equal")





# QUE 4
x = int(input("enter ur age : "))

if x >= 18:
    print("Can Vote")
else: 
    print("Cannot Vote")



# QUE 5
x = int(input("enter a no. : "))
if x % 5 == 0 and x % 11 == 0 :
    print("Divisible by both")
else :
    print("Not divisible by both")




# QUE 6
x = input("Enter an alphabet: ").lower()
if x in "aeiou":
    print("Vowel")
else:
    print("Consonant")





# QUE 7
x = input("Enter password: ")
if x == "python123" :
    print("Correct Password")
else : 
    print("Incorrect Password")





# QUE 8
x = int(input("enter 1st no. : "))
y = int(input("enter 2nd no. : "))
z = int(input("enter 3rd no. : "))

if x >= y and x >= z:
    print(x, "is greatest")
elif y >= x and y >= z:
    print(y, "is greatest")
else:
    print(z, "is greatest")





# QUE 9   
x = (input("enter a character : "))
if x .islower():
    print("Lowercase")
elif x .isupper() :
    print("Uppercase")
elif x .isdigit() : 
    print("Digit")
else:
    print("Special character")





# QUE 10
x = int(input("enter 1st no. : "))
y = int(input("enter 2nd no. : "))
z = input("enter operator : ")

if z == "+" :
    print ( x + y )
elif z == "-" :
    print ( x - y )
elif z == "*" :
    print ( x * y )
elif z == "/" :
    if y == 0 :
        print("Cannot perform operation with zero!")
    else:
         print( x / y )
else:
    print("Invalid operator! Please use a valid operator.")