# arithmetic operators
a= 8
b=5
print(a + b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #remainder
print(a**b) #a^b



#relational operators
a= 100
b=80
print(a==b) #false
print(a!=b) #true
print (a>=b) #true
print (a>b) #true
print(a<=b) #false
print(a<b) #false



#assignment operators
num= 10
# num= num+20, similar to num +=20
num +=20 #adds 
print("num:", num)#30
num -=20 # substract
print("num:", num)#10
num *=5 #multiply 
print("num:", num)#50
num /=5 #divides
print("num:", num)#10
num %=4 #remainder
print("num:", num)#2
num **=5 #power operator 2^5
print("num:", num)#32



#logical operators
a= 30
b= 10
print(not a>b)#false
print(not a<b)#true

val1= True
val2= True
print("AND operator:", val1 and val2)#true

val1= True
val2= False
print("AND operator:", val1 and val2)#false

print("AND operator:", (a==b) and (a>b))#false


val1= True
val2= True
print("OR operator:", val1 or val2)#true

val1= True
val2= False
print("OR operator:", val1 or val2)#true

val1= False
val2= False
print("OR operator:", val1 or val2)#false

print("OR operator:", (a==b) or (a>b))#true

