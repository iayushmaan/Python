# Dictionary Methods:
# 1. myDict.keys() — Returns all keys.
# 2. myDict.values() — Returns all values.
# 3. myDict.items() — Returns all (key, value) pairs as tuples.
# 4. myDict.get("key") — Returns the value associated with the specified key.
# 5. myDict.update(newDict) — Inserts the specified items into the dictionary.



info = {
    "key" : "value",
    "name" : "ayushmaan",
    "age" : 18,
    "learning" : "Python",
    "is_adult" : True,
    "marks" : 83.6,
    "subjects" : {
        "phy" : 81,
        "chem" : 89,
        "maths" : 85
    },
    "topics" : ("dict", "sets")
}

print(info.keys())

print(list(info.keys()))

print(len(info)) #or-->
print(len(list(info.keys())))



print(info.values())
print(list(info.values()))



print(info.items())

print(list(info.items()))

pairs = list(info.items())
print(pairs[0])

pairs = list(info.items())
print(pairs[5])



print(info["name"])
print(info.get("name"))

print(info["namee"]) #error
print(info.get("namee")) #none

# dict.get(key) is safer than dict[key] because if the key does not exist, dict[key] raises a KeyError and stops the program's normal execution. In contrast, dict.get(key) returns None by default, allowing the program to continue running.




info.update({"city" : "sln"})
print(info) #or-->

new_dict = {"city" : "sln"}
info.update(new_dict)
print(info)



info.update({"city" : "sln" , "postal_code" : 228001})
print(info) #or-->

new_dict = {"city" : "sln" , "postal_code" : 228001}
info.update(new_dict)
print(info)

# dict.update(new_dict) adds new key-value pairs to the existing dictionary. If a key already exists, its value is updated with the new value.