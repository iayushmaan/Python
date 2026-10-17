# Positive indexing starts counting from 0 (left to right).

str = "Python Language"

print(str[4:8])
print(str[7:15]) # or-->
print(str[7:len(str)]) # or-->
print(str[7:]) #[7:len(str)]

print(str[:4]) #[0:4]




# Negative indexing starts counting from -1 (right to left).
str = "Physics"

print(str[-6:-2])
print(str[-6:4]) # If slicing starts with a negative index, Python counts from the right side, but the index is equivalent to its corresponding positive index from the left.
