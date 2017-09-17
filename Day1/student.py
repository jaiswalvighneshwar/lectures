from college_user import CollegeUser

class Student(CollegeUser):
# for a class definition the self parameter
	def __init__(self,name,gender,roll,marks):
		super(Student,self).__init__(name,gender)		
		#self.name = name			# this will not need to be done as it is done by CollegeUserinit
		#self.gender = gender
		self.roll = roll
		self.marks = marks

	def get_name_roll(self):
		return (self.name,self.roll)

	def get_grade(self):
		marks = self.marks
		if marks >100 or marks <0:
	    		return "Marks ", str(marks) , " is invalid"
		elif marks >= 70:
			return "Grade is A"
		elif marks >= 60:
		    return "Grade is B"
		elif marks >=40 :
		      return "Grade is C"
		else :
		    return "You have Failed"

	def get_details(self):
		#methd overriding , overriding from super class
		details = super(Student,self).get_details()
		details+= '\n Roll: {0}\n Marks: {1}'.format(self.roll,self.marks)
		return details
