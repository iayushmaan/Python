# Lists are mutable, whereas strings and tuples are immutable

marks = [89.4, 85.2, 79.8, 49.5, 93.9, 99.7]
print (marks)
print(type(marks))
print(len(marks))
print(marks[0])
print(marks[5])
print(marks[-2])

student = ["ayushmaan" , 84.6, 18, "Sultanpur"]
print(student[1])
student[1] = 65.2
print(student)