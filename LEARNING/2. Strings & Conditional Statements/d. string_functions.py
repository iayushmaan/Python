# str.endswith(" ")  #returns true if string ends with substr
# str.capitalize  #capitalizes 1st char
# str.replace(old, new) #replaces all occurrences of old with new
# str.find(word) #returns 1st index of 1st occurrence
# str.count(" ") #counts the occurrence of substr in string



str1 = "Small steps every day lead to big results"
print(str1.endswith("ults")) # true
print(str1.endswith("hello")) # false

str2 = "small steps every day lead to big results"
print(str2.capitalize()) # capitalize() converts the first character of a string to uppercase, but it does not change the original string
# To permanently update the string, assign the modified value back to the same variable.
str2= str2.capitalize()
print(str2)

str3 = "Small steps every day lead to big results"
print(str3.replace("a", "o"))
print(str3.replace("day", "night"))

str4 = "Small steps every day lead to big results"
print(str4.find("e"))
print(str4.find("day"))
print(str4.find("Hello")) # does not exist, we get invalid index

str5 = "Small steps every day lead to big results"
print(str5.count("every"))
print(str5.count("e"))
print(str5.count("night")) # does not exist, we get 0