# QUE 1
units = int(input("Enter electricity units: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

print("Electricity Bill = Rs.", bill)





# QUE 2 
x = int(input("enter a no. : "))
if x < 10 or x > 50:
    print("not in range")
elif x >= 10 and x <= 50:
    print("in range")





# QUE 3
username = input("Enter your username: ")

if len(username) < 5 or len(username) > 12:
    print("Invalid Username")

elif username[0].isdigit():
    print("Invalid Username")

elif " " in username:
    print("Invalid Username")

elif "admin" in username.lower():
    print("Invalid Username")

else:
    print("Valid Username")