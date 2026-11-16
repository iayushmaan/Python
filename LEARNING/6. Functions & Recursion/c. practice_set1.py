# QUE 1
cities = ["sultanput", "ayodhya", "raebareli", "kanpur", "noida"]
heroes = ["ironman", "spiderman", "thor", "hulk"]

def len_list(list):
    print(len(list))

len_list(cities)
len_list(heroes)






# QUE 2
fruits = ["mango", "banana", "papaya", "apple", "grapes"]

def list_items(list):
    for item in list:
        print(item, end =" ")

list_items(fruits)
print()






# QUE 3
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(7)






# QUE 4
def convertor(usd):
    inr = usd * 93.85
    print(usd, "USD =", inr ,"INR")

convertor(73)





# QUE 5
def value():
    value = int(input("enter a no. : "))
    if value % 2 == 0:
        print("EVEN")
    else:
        print("ODD")

value()