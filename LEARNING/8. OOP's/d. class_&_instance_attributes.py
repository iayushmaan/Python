# =================================
#    CLASS & INSTANCE ATTRIBUTES
# =================================

# Attributes = Variables that store data.

# There are two types of attributes:

# 1. Class Attributes
# Class attributes belong to the class.
# They are generally shared by all objects.
# Access using ClassName.attribute.

# Example:
# Student.school

# Class attributes can have the same value
# for multiple objects.
# Example: All students can have the same school name.

# 2. Instance Attributes
# Instance attributes belong to a particular object.
# Each object can have its own separate values.
# Usually created using self inside __init__().
# Access using object.attribute.

# Example:
# s1.name

# Instance attributes can have different values
# for different objects.
# Example: Every student can have a different name and age.

# ==========================
#    IMPORTANT DIFFERENCE   
# ==========================

# Class Attribute = Common information
# Instance Attribute = Individual information

# Class Attribute  = Class.attr
# Instance Attribute = obj.attr

# Remember:
# Class Attribute = Shared
# Instance Attribute = Object-specific



class Student:

    college_name = "ABC College"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in database")

s1 = Student("Ayushmaan", 84)
print(s1.name, s1.marks)
print(Student.college_name)

s2 = Student("Dhairya", 96)
print(s2.name, s2.marks)
print(s2.college_name)

s3 = Student("Ambuj", 89)
print(s3.name, s3.marks)
print(Student.college_name)










class Student:

    college_name = "ABC College"
    name = "Anonymous"  #class attr

    def __init__(self, name, marks):
        self.name = name   #obj attr > class attr
        self.marks = marks
        print("adding new student in database")

s1 = Student("Ayushmaan", 84)
print(s1.name)