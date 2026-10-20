# QUE 1

# num = 1
# while num <= 100:
#     print(num)
#     num += 1



# QUE 2

# num = 100
# while num >= 1:
#     print(num)
#     num -=1




# QUE 3

# n = int(input("Enter the number : "))
# i = 1
# while i <=10:
#     print(n * i)
#     i += 1




# QUE 4

# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# heroes = ["superman", "batman", "spiderman", "ironman", "venom"]

# #traverse
# idx = 0
# while idx < len(num):
#     print(num[idx])
#     idx += 1

# idx = 0
# while idx < len(heroes):
#     print(heroes[idx])
#     idx += 1





# QUE 5

num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36
i = 0
while i < len(num):
    if num[i] == x:
       print("FOUND at idx : ", i)
    i += 1