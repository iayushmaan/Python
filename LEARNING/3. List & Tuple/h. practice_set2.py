# A palindrome is a word, number, or sequence that reads the same forward and backward.

list = [1, 2, 3, 2, 1]
copy_list = list.copy()
list.reverse()

if(list == copy_list):
    print("Palindrome")
else:
    print("not a Palindrome")




list = [1, 2, 3, 2, 7]
copy_list = list.copy()
list.reverse()

if(list == copy_list):
    print("Palindrome")
else:
    print("not a Palindrome") 