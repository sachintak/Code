# Accept the marks of 6 students and print them into sorted manner, marks must be integer

s1 = int(input("Enter the Marks of student 1: "))
s2 = int(input("Enter the Marks of student 2: "))
s3 = int(input("Enter the Marks of student 3: "))
s4 = int(input("Enter the Marks of student 4: "))
s5 = int(input("Enter the Marks of student 5: "))
s6 = int(input("Enter the Marks of student 6: "))

listOfStudentMarks = [s1, s2, s3, s4, s5, s6]
listOfStudentMarks.sort() # sort the list in asscending order, if want to arrange in descending then reverse the list
print(listOfStudentMarks)

listOfStudentMarks.reverse() # list is now sorted in descending order
print(listOfStudentMarks)

