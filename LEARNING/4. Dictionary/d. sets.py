# Sets in Python

# 1. Definition:
# A set is an unordered collection of unique elements.

# 2. Properties of Sets:
# - Sets do not store duplicate elements.
# - Set elements must be hashable.
# - Sets are unordered and do not guarantee a fixed order of elements.

# 3. Example:
# nums = {1, 2, 3, 4}

# 4. Duplicate Elements:
# Repeated elements are stored only once.
# Example: set2 = {1, 2, 2, 2}  ->  {1, 2}

# 5. Empty Set:
# Use set() to create an empty set.
# Example: null_set = set()

# Note:
# {} creates an empty dictionary, not an empty set.


# Elements allowed in a Python set:
# bool, int, float, str
# tuple (if all elements are hashable)

# Elements not allowed in a Python set:
# list, dict (because they are unhashable)

# List, Dictionary, Sets--> MUTABLE
# Tuple, Strings, Sets Element--> IMMUTABLE




collection = {1, 2, 3, 4, 5, "hello","world" ,2 ,4 ,3 ,3}
print(collection)
print(type(collection))
print(len(collection))


coll = set()
print(type(coll)) #empty set; syntax

