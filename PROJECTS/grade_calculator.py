# GRADING SYSTEM:
# 91 - 100  : Grade A
# 81 - 90   : Grade B
# 71 - 80   : Grade C
# 61 - 70   : Grade D
# 51 - 60   : Grade E
# 0 - 50    : Grade F
# Below 0 or Above 100 : INVALID MARKS


marks = int(input("Enter your marks: "))
if(marks>100) or (marks<0):
    print("INVALID MARKS")
elif(marks>90):
    print("Grade A")
elif(marks>80) and (marks<=90):
    print("Grage B")
elif(marks>70) and (marks<=80):
    print("Grade C")
elif(marks>60) and (marks<=70):
    print("Grade D")
elif(marks>50) and (marks<=60):
    print("Grade E")
else:
    print("Grade F")