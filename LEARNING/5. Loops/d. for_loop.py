# LOOPS IN PYTHON
# Loops are used for sequential traversal of sequences like lists, strings, and tuples.
# They help execute a block of code repeatedly.

# FOR LOOP
# Used to iterate over each element of a sequence.
# Executes the block of code for every element.

# FOR LOOP WITH ELSE
# The else block executes when the loop completes normally.
# If the loop terminates using break, the else block is not executed.
# A normal print() statement after the loop executes even if the loop stops using break.
# The else block is useful to check whether the loop completed without break.

# ITERATION
# One complete round of a loop is called an iteration.
# Each time the loop body executes, one iteration is completed.




nums = [1, 4, 9, 32, 534, 85, 69, 72]
for val in nums:
    print(val)


veggies = ["tomato", "potato", "ladyfinger", "brinjal"]
for val in veggies:
    print(val)


tup = (1, 3, 8, 5, 0)
for num in tup:
    print(num)


str = "ayushmaan singh"
for char in str:
    print(char)
else:
    print("end")









# FOR LOOP WITH ELSE

# Example 1: Else executes when loop completes normally.

for i in range(5):
    print(i)
else:
    print("Loop completed successfully")

# Output:
# 0
# 1
# 2
# 3
# 4
# Loop completed successfully



# Example 2: Else does not execute when loop terminates using break.

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed successfully")

# Output:
# 0
# 1
# 2



# Example 3: Normal print executes even after break,
# but else block does not execute.

for i in range(5):
    if i == 2:
        break
    print(i)
else:
    print("Loop completed")

print("END")

# Output:
# 0
# 1
# END