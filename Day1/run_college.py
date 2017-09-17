from student import Student
from professor import Professor
from xyz.supercoders.salcal.calc import SalCal
from xyz.supercoders.salcal.calc import InvalidDaysError


s1 = Student(name='mehul',gender='m',marks=78,roll=10)
s2 = Student(name = 'jane',gender = 'f', marks = 90 , roll = 11)
p1 = Professor(name = 'mark',gender = 'm', subjects=['Physics','Maths'], cost = 2000,days=23)



print p1.subjects
print s1.get_details()
print s2.get_details()

print p1.get_details()

try:
	print SalCal.calc(p1)
except TypeError as e:
	print e
	#print 'Only Salaried Individuals please!'
except ValueError:
	print 'Please check your values' 

except InvalidDaysError as e:
	print e
# new changes to the process  in future


	print SalCal.calc(s1)   #should give an error

# calc should woork for any salaried person
