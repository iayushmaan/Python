# if
# elif
# else 


age = 21

if (age >= 18):
    print("can vote")
    print("can drive") # or-->

if (True):
    print("can vote")
    print("can drive")


light = "green"

if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("look")
# An if statement must come before an elif statement

num= 5
if(num>2):
    print("greater than 2")
if(num>3):
    print("greater than 3")

num2= 5
if(num2>2):
    print("greater than 2")
elif(num2>3):
    print("greater than 3")
# An if statement checks each condition independently, so multiple conditions can be true and all their corresponding statements will execute. However, in an if-elif chain, once a condition is true, the remaining conditions are skipped.

light = "neon"

if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif (light=="yelllow"):
    print("look")
else:
    print("light is broken")

print("end of code")
# If all the above conditions are false, the else block will execute.



age= 17
if(age>=18):
    print("can vote") # Indentation means spaces at the beginning of a line. It is very important in Python because it defines blocks of code.
else:
    print("CANNOT VOTE")




marks = 81
if(marks>=90):
     Grade = "A"
elif(marks>=80 and marks<90):
     Grade = "B"
elif(marks>=70 and marks<80):
     Grade = "C"
else:
     Grade = "D"

print ("Grade of the student-->", Grade ) 





marks = int(input("enter student marks : "))
if(marks>=90):
     Grade = "A"
elif(marks>=80 and marks<90):
     Grade = "B"
elif(marks>=70 and marks<80):
     Grade = "C"
else:
     Grade = "D"

print ("Grade of the student-->", Grade ) 



# Nesting
age= 81
if(age>=18):
    if(age>=80):
        print("cannot drive anymore")
    else:
        print("can drive")
else:
    print("cannot drive")