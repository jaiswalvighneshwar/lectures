'''from student_ops import get_details as gd , get_grade as gg

name = raw_input ("Enter Student Name: ")
gender = raw_input ("Enter Student gender: ")
roll = raw_input ("Enter Student roll: ")
marks = int(raw_input ("Enter Student marks: "))

print gd(name,gender,roll)
print gg(marks)'''

from student import Student
from professor import Professor
s1 = Student('VJ123','Male',10,29) 
s2 = Student('Jane','Female',23,90)

'''print id(s1)
print id(s2)

print type (s1)
print type (s2)

s1.name = 'Vighneshwar'
s1.gender = 'Male'
s1.marks = 89
s1.roll = 10

s2.name = 'Jane'
s2.gender = "Female"
s2.roll = 34
s2.marks = 90
s2.address = 'Andheri\''''

print s1.name
print s2.roll
print s1.get_grade()
print s2.get_grade()



