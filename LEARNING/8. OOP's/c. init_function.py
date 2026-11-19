# =========================
#    __init__() FUNCTION
# =========================

# __init__() is a special method in Python.
# It is commonly known as a constructor.


# Constructor is automatically executed when an object is created.
# Constructor is used to initialize object attributes.

# Object creation triggers __init__().

# self refers to the current instance of the class.
# self is used to access attributes and methods belonging to the current object.

# Attributes = Variables that store data related to a class or object.
# Attributes represent the properties or information of an object.

# Example:
# name and age are attributes.

# IMPORTANT:
# Constructor = __init__()
# self = Reference to current object
# fullname = Parameter
# self.name = Object attribute




# class Student:
#     name = "Ayushmaan Singh"
#     def __init__(self):
#         print(self)
#         print("adding new student in database")

# s1 = Student()
# print(s1) # similar to self





# class Student:
#     def __init__(self,name):
#         self.name = name
#         print("adding new student in database")

# s1 = Student("Ayushmaan")
# print(s1.name)

# s2 = Student("Ambuj")
# print(s2.name)

# s3 = Student("Dhairya")
# print(s3.name)





class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in database")

s1 = Student("Ayushmaan", 84)
print(s1.name, s1.marks)

s2 = Student("Ambuj", 85)
print(s2.name, s2.marks)

s3 = Student("Dhairya", 92)
print(s3.name, s3.marks)










class Student:

    #default constructors
    def __init__(self):
            pass
    
    #parameterized constructors
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in database")

s1 = Student("Ayushmaan", 84)
print(s1.name, s1.marks)

s2 = Student("Ambuj", 85)
print(s2.name, s2.marks)

s3 = Student("Dhairya", 92)
print(s3.name, s3.marks)