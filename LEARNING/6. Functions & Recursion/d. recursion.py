# =============
#   RECURSION
# =============

# Recursion is a process in which a function calls itself repeatedly.
# When a function calls itself, it is called Recursion.


# BASE CASE:
# Base case is the condition that stops the recursion.
# It prevents the function from calling itself infinitely.
# When the base condition becomes True, the function stops.


# RECURSIVE CALL:
# A recursive call is when a function calls itself.
# In recursion, the function calls itself with a smaller or simpler input.


# IMPORTANT:
# The same task can be performed using both Loops and Recursion.
# Loops and Recursion are two different ways to repeat a task.
# Loops use for and while statements.
# Recursion uses a function that calls itself.
# Both can be used to solve many similar problems.







#1
# recursive function
def show(n):
    if n == 0: # base case
        return
    print(n)
    show(n-1)

show(9)




# ---->
def show(n):
    if n == 0:
        return
    print(n)
    show(n-1)
    print("end")

show(9)     #output--> 9 8 7 6 5 4 3 2 1 end end end end end end end end end 









#2
def fact(n):
    if n == 1 or n == 0:
        return 1
    return fact(n-1) * n

print(fact(5))