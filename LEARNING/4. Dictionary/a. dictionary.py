info = {
    "key" : "value",
    "name" : "ayushmaan",
    "age" : 18,
    "learning" : "Python",
    "is_adult" : True,
    "marks" : 83.6,
    "subjects" : ["Physics", "Maths"],
    "topics" : ("dict", "sets")
}

print(info)
print(type(info))

print(info["learning"])
print(info["is_adult"])

info["name"] = "Ayushmaan"
info["surname"] = "Singh"
print(info)



null_dict = {}
print(null_dict)
null_dict["OS"] = "Mac"
print(null_dict)







# Dictionary Keys: Keys must be hashable (generally immutable) objects, such as strings, numbers, and tuples containing only hashable elements.
# Dictionary Values: Values can be of any data type, including strings, numbers, lists, tuples, dictionaries, and more.
# Hashable: An object is hashable if its hash value remains constant during its lifetime. Hashable objects can be used as dictionary keys and set elements.

# List, Dictionary--> MUTABLE
# Tuple, Strings--> IMMUTABLE

# Duplicate keys are not allowed in a dictionary. If the same key is used more than once, the last value overwrites the previous value.
