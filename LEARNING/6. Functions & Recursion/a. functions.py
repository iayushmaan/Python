
# ==========================================
# FUNCTIONS IN PYTHON
# ==========================================

# A function is a block of statements that performs a specific task.
# Functions help to avoid code repetition and make code reusable.
# They make code more organized and easier to understand.


# ==========================================
# TYPES OF FUNCTIONS IN PYTHON
# ==========================================

# Python functions are divided into two main types:
# 1. Built-in Functions
# 2. User-defined Functions


# ==========================================
# 1. BUILT-IN FUNCTIONS
# ==========================================

# Built-in functions are predefined functions in Python.
# They are already available in Python.
# We can use them directly without defining them.

# Examples:
# print() - Displays output.
# len()   - Returns the length of an object.
# type()  - Returns the data type of an object.
# range() - Generates a sequence of numbers.

# END PARAMETER

# The end parameter is used to print multiple values on the same line.
# By default, print() adds a newline after each output.
# end=" " adds a space instead of a newline.
# It helps to display multiple values on the same line.

# ==========================================
# 2. USER-DEFINED FUNCTIONS
# ==========================================

# User-defined functions are created by the programmer.
# They are defined using the def keyword.
# They are used to perform specific tasks.
# They help reduce code repetition and make code reusable.


# ==========================================
# FUNCTION DEFINITION
# ==========================================

# A function is created using the def keyword.
# Parameters are variables written inside the function definition.

# SYNTAX:
# def function_name(parameters):
#     # Some work
#     return value


# ==========================================
# FUNCTION CALL
# ==========================================

# A function is executed by calling its name with parentheses.
# Arguments are actual values passed during a function call.


# ==========================================
# RETURN STATEMENT
# ==========================================

# return is used to send a result back to the function caller.
# It allows us to store and reuse the returned value.
# It also terminates the function execution.


# ==========================================
# REDUNDANT CODE
# ==========================================

# Redundant means unnecessary or repeated code.
# Functions help reduce code repetition.
# They make code reusable and easier to maintain.


# ==========================================
# EXAMPLES OF USER-DEFINED FUNCTIONS
# ==========================================


# ------------------------------------------
# 1. FUNCTION WITH PARAMETERS AND RETURN
# ------------------------------------------

def cal_sum(a, b):
    total = a + b
    print(total)
    return total

cal_sum(2, 6)

# Function can be called multiple times.

cal_sum(7, 15)

cal_sum(18, 24)


# ALTERNATIVE WAY:

def sum_calc(a, b):
    return a + b

result = sum_calc(812, 923)
print(result)

# a, b = Parameters
# 812, 923 = Arguments
# result = Variable storing the returned value


# ------------------------------------------
# 2. SIMPLE FUNCTION
# ------------------------------------------

# A function without parameters.

def hello_print():
    print("hello")

hello_print()
hello_print()
hello_print()

# The same function can be called multiple times.


# ------------------------------------------
# 3. FUNCTION WITHOUT RETURN
# ------------------------------------------

def hello_world():
    print("singh")

x = hello_world()
print(x)

# Output:
# singh
# None

# If a function does not have a return statement,
# Python automatically returns None.


# ------------------------------------------
# 4. AVERAGE OF 3 NUMBERS
# ------------------------------------------

def avg(a, b, c):
    x = (a + b + c) / 3
    print(x)
    return x

avg(2, 6, 8)

# Calculates and returns the average of three numbers.