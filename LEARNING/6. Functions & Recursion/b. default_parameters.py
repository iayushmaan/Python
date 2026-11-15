# DEFAULT PARAMETERS
# Default parameters are parameters that have default values.
# The default value is used when no argument is passed.
# If an argument is passed, the default value is overridden.
# Default parameters make function arguments optional.


#====================
#  Important Points
#====================
# If no argument is passed, the default value is used.
# If an argument is passed, it replaces the default value.
# Parameters with default values must come after non-default parameters.




def prod_cal(a=3,b=4):
    print(a*b)
    return(a*b)
prod_cal()

# OR--> 

def cal_prod(a, b=4):
    print(a*b)
    return(a*b)
cal_prod(3)


# DEFAULT PARAMETERS
# Parameters with default values must come after non-default parameters.
# Non-default parameters must be placed before default parameters.

# Correct:
# def func(a, b=5):
#     pass

# Incorrect:
# def func(a=5, b):
#     pass