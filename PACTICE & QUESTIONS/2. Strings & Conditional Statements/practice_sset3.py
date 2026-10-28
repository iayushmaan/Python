# # QUE 1
# x = input("enter username : ")
# y = input("enter password : ")

# if x == "admin" and y == "python123":
#     print("login successful")
# else:
#     print("check your input")



# QUE 2
x = int(input("shopping amount : "))
if x < 1000:
    print("no discount")
    print(x)
elif x >= 1000 and x < 3000:
    discount = x * 5 / 100
    final_amount = x - discount
    print("Discount:", discount)
    print("Final amount:", final_amount)
elif x >= 3000 and x < 5000:
    discount = x * 10 / 100
    final_amount = x - discount
    print("Discount:", discount)
    print("Final amount:", final_amount)
else:
    discount = x * 20 / 100
    final_amount = x - discount
    print("Discount:", discount)
    print("Final amount", final_amount)