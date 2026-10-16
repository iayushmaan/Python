# List Methods:
# 1. append(el): Adds one element at the end of the list.
# 2. sort(): Sorts the list in ascending order.
# 3. sort(reverse=True): Sorts the list in descending order.
# 4. reverse(): Reverses the order of elements in the list.
# 5. insert(idx, el): Inserts an element at a specific index.
# 6. remove(el): Removes the first occurrence of an element from the list.
# 7. pop(idx): Removes the element at a specific index.

list = [24, 23, 74, 69, 54, 34, 89, 98, 13]

list.append(49) # this is called mutation of list, mutation is possible in list.
print(list)

list.sort()
print(list)

list.sort(reverse=True)
print(list)






list = ["mango", "banana", "papaya", "litchi", "apple"]

list.append("guava")
print(list)

list.sort()
print(list)

list.sort(reverse=True)
print(list)






# list.reverse()
list = [24, 23, 74, 69, 54, 34, 89, 98, 13]
list.reverse()
print(list)






# list.insert(index, element)
list = [24, 23, 74, 69, 54, 34, 89, 98, 13]
list.insert(5,41)
print(list)





#list.remove(el)
#Removes only the first occurrence of an element if it appears multiple times in the list.
list = [24, 23, 74, 69, 54, 34, 89, 98, 13]
list.remove(69)
print(list)





#list.pop(idx)
list = [24, 23, 74, 69, 54, 34, 89, 98, 13]
list.pop(5)
print(list)