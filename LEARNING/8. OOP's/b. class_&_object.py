# ==============================
# CLASS & OBJECT IN PYTHON
# ==============================

# Class is a blueprint for creating objects.

# Blueprint means a design or structure.

# Class defines attributes and methods.

# Object is an instance of a class.

# We can create multiple objects from one class.

# Example:
# class Student:
#     name = "karan kumar"

# Creating an object
# s1 = Student()

# Accessing attribute using object
# print(s1.name)

# Output: karan kumar

# IMPORTANT:
# Class = Blueprint
# Object = Instance of a class
# Student = Class name
# s1 = Object name
# name = Attribute




class Student:
    name = "Ayushmaan Singh"

s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name) # same output




class Car:
    colour = "Blue"
    brand = "Mercedes"

car = Car()
print(car.colour)
print(car.brand)