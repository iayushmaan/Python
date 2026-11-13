# RANGE() FUNCTION
# The range() function generates a sequence of numbers.
# It starts from 0 by default and increments by 1.
# It stops before the specified stop value.
# It is commonly used with for loops.

# SYNTAX:
# range(start, stop, step)
# start: Starting value (optional, default is 0).
# stop: Ending value (excluded, required).
# step: Difference between numbers (optional, default is 1).




# LINEAR SEARCH
# Linear search is used to find an element in a list.
# It checks each element one by one from the beginning.
# If the target element is found, its index is returned.
# If the target element is not found, -1 is returned.
# It works on both sorted and unsorted lists.
# No sorting is required before searching.

# TIME COMPLEXITY
# Best Case: O(1) - Element found at the first position.
# Worst Case: O(n) - Element found at the last position or not found.
# Space Complexity: O(1)
# Uses constant extra memory regardless of the list size.






# seq = range(10)

# for i in seq:
#     print(i) #or-->

# for i in range(10): #range(stop)
#     print(i)




# for i in range(3,10): #range(start, stop)
#     print(i)




# for i in range(3, 20, 3): #range(start, stop, step)
#     print(i)





# # QUE 1 #odd numbers
# for i in range(1, 10, 2):
#     print(i)

# #QUE 2 #even numbers
# for i in range(0, 11, 2):
#     print(i)






# PASS STATEMENT
# pass is a null statement that does nothing when executed.
# It is used as a placeholder for future code.
# It allows us to write an empty block of code without getting an error.
# pass does not terminate or skip the loop.

for i in range(10):
    pass  # Does nothing; loop continues normally.

print("Loop completed")

# Output: Loop completed





# DIFFERENCE BETWEEN PASS, CONTINUE AND BREAK:-
# pass: Does nothing; acts as a placeholder.
# continue: Skips the current iteration and moves to the next iteration.
# break: Terminates the loop immediately.