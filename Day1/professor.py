from college_user import CollegeUser
from xyz.supercoders.salcal.calc import SalariedIndividual
class Professor(CollegeUser,SalariedIndividual):

	def __init__(self,name,gender,days,cost,subjects=[]):
		super(Professor,self).__init__(name,gender)
		#self.name = name             # this will not need to be done as it is done by CollegeUserinit
		#self.gender = gender
		self.subjects= subjects
		self.days = days
		self.cost = cost

	def get_details(self):
		details = super(Professor,self).get_details()
		details+= "\n" + ('|'.join(self.subjects))
		return details

	def get_days(self):
		return self.days

	def get_cost(self):
		return	self.cost
