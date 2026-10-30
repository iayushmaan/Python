# # QUE 1
# x = input("enter username : ")
# y = input("enter password : ")

# if x == "admin" and y == "python123":
#     print("login successful")
# else:
#     print("check your input")



# # QUE 2
# x = int(input("shopping amount : "))
# if x < 1000:
#     print("no discount")
#     print(x)
# elif x >= 1000 and x < 3000:
#     discount = x * 5 / 100
#     final_amount = x - discount
#     print("Discount:", discount)
#     print("Final amount:", final_amount)
# elif x >= 3000 and x < 5000:
#     discount = x * 10 / 100
#     final_amount = x - discount
#     print("Discount:", discount)
#     print("Final amount:", final_amount)
# else:
#     discount = x * 20 / 100
#     final_amount = x - discount
#     print("Discount:", discount)
#     print("Final amount", final_amount)





# # QUE 3
# user_balance = 5000
# x = int(input("enter withdrawl amount : "))
# if x <= 0:
#     print("error")
# elif x > user_balance:
#     print("not sufficient balance")
# else:
#     print("successfully withdrawal")
#     print("remaining balance :", user_balance - x)






# QUE 4
x = int(input("enter a no. : "))
if x >= 10 and x <= 50:
    print("The number is between 10 and 50.")
else:
    print("The number is out of range.")