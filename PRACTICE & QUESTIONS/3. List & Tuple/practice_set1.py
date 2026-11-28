# QUE 1
# Creating a list
my_list = [10, 20, 30, 40, 50]

# Creating a tuple
my_tuple = (10, 20, 30, 40, 50)

# Length
print(len(my_list))
print(len(my_tuple))

# Maximum and Minimum
print(max(my_list))
print(min(my_list))

print(max(my_tuple))
print(min(my_tuple))

# Updating list
my_list[1] = 100
print(my_list)

# Updating tuple
my_tuple[1] = 100
print(my_tuple)





# QUE 2

# Creating a list
my_list = ["Apple", "Mango", "Banana", "Orange", "Grapes"]

# Creating a tuple
my_tuple = ("Kiwi", "Papaya", "Cherry", "Pineapple", "Mango")

# Printing List and Tuple
print(my_list)
print(my_tuple)

# Adding element to List
my_list.append("Watermelon")
print(my_list)

# Removing element from List
my_list.remove("Banana")
print(my_list)

# Checking Mango
print("Mango" in my_list)
print("Mango" in my_tuple)

# Counting elements
print(len(my_list))
print(len(my_tuple))

# Final List and Tuple
print(my_list)
print(my_tuple)





# QUE 3

# Creating a list
my_list = [15, 22, 8, 31, 44, 17, 50, 9, 26, 13]

# Printing even numbers
print("Even Numbers:")
for i in my_list:
    if i % 2 == 0:
        print(i)

# Printing odd numbers
print("Odd Numbers:")
for i in my_list:
    if i % 2 != 0:
        print(i)

# Sum of even numbers
even_sum = 0
for i in my_list:
    if i % 2 == 0:
        even_sum += i

print("Sum of Even:", even_sum)

# Sum of odd numbers
odd_sum = 0
for i in my_list:
    if i % 2 != 0:
        odd_sum += i

print("Sum of Odd:", odd_sum)

# Sorting List
my_list.sort()
print("Sorted List:", my_list)

# Converting List into Tuple
my_tuple = tuple(my_list)

print("Final List:", my_list)
print("Final Tuple:", my_tuple)






# QUE 4

# Creating a List
my_list = [10, 20, 30, 40, 50, 20, 60, 70, 80, 90]

# Second Largest
a = sorted(set(my_list))
print("Second Largest:", a[-2])

# Second Smallest
print("Second Smallest:", a[1])

# Counting elements
n = int(input("Enter a number to count: "))
print("Count:", my_list.count(n))

# Reversing List
my_list.reverse()
print("Reversed List:", my_list)

# Copying List
new_list = my_list.copy()
print("Copied List:", new_list)

# Converting List into Tuple
my_tuple = tuple(new_list)

# Final Output
print("Final List:", new_list)
print("Final Tuple:", my_tuple)






# QUE 5

# Creating a List
my_list = [10, -20, 30, -40, 50, -60, 70, -80, 90, -100]

# Creating empty Lists
positive = []
negative = []

# Separating positive and negative numbers
for i in my_list:
    if i > 0:
        positive.append(i)
    elif i < 0:
        negative.append(i)

# Counting numbers
print("Positive Count:", len(positive))
print("Negative Count:", len(negative))

# Sum of numbers
print("Positive Sum:", sum(positive))
print("Negative Sum:", sum(negative))

# Converting into Tuples
pos_tuple = tuple(positive)
neg_tuple = tuple(negative)

# Printing Lists
print("Positive List:", positive)
print("Negative List:", negative)

# Printing Tuples
print("Positive Tuple:", pos_tuple)
print("Negative Tuple:", neg_tuple)





# QUE 6

# Creating a List
my_list = [12, 15, 20, 9, 30, 25, 18, 7, 21, 10]

# Creating empty Lists
divisible = []
square = []

# Finding numbers divisible by 3
for i in my_list:
    if i % 3 == 0:
        divisible.append(i)

# Finding square of numbers
for i in divisible:
    square.append(i ** 2)

# Maximum and Minimum
print("Maximum:", max(square))
print("Minimum:", min(square))

# Converting into Tuples
t1 = tuple(divisible)
t2 = tuple(square)

# Printing Results
print("Original List:", my_list)
print("Divisible by 3:", divisible)
print("Square List:", square)

print("First Tuple:", t1)
print("Second Tuple:", t2)






# QUE 7

# Creating a List
my_list = [10, 20, 30, 20, 40, 50, 30, 60, 70, 10]

# Creating empty List
duplicate = []

# Finding duplicate elements
for i in my_list:
    if my_list.count(i) > 1:
        if i not in duplicate:
            duplicate.append(i)

# Removing duplicates
unique = list(set(my_list))

# Sorting in descending order
unique.sort(reverse=True)

# Finding sum
print("Sum:", sum(unique))

# Converting into Tuples
t1 = tuple(duplicate)
t2 = tuple(unique)

# Printing Results
print("Original List:", my_list)
print("Duplicate List:", duplicate)
print("Unique List:", unique)

print("Duplicate Tuple:", t1)
print("Unique Tuple:", t2)






# QUE 8

# Creating a List
my_list = [12, 7, 15, 11, 20, 13, 9, 17, 25, 19]

# Creating empty List
prime = []

# Finding prime numbers
for i in my_list:
    if i > 1:
        count = 0

        for j in range(1, i + 1):
            if i % j == 0:
                count += 1

        if count == 2:
            prime.append(i)

# Counting prime numbers
print("Total Prime Numbers:", len(prime))

# Sum of prime numbers
print("Sum:", sum(prime))

# Largest and Smallest
print("Largest:", max(prime))
print("Smallest:", min(prime))

# Reversing List
prime.reverse()

# Converting into Tuple
my_tuple = tuple(prime)

# Printing Results
print("Original List:", my_list)
print("Prime List:", prime)
print("Prime Tuple:", my_tuple)