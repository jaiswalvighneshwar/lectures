class Author:
	
	count = 0	

	def __init__(self,name,gender,rating):
		self.name = name
		self.set_gender(gender)			#__ changes the attribute of gender and rating
		self.__rating = rating				#__ makes the attribute 
		Author.count += 1

	
	def get_details(self):
		return "Name: {0}\nGender: {1}\nRating: {2}".format(self.name,self.__gender,self.__rating)
	
	def set_gender(self,gender):
		if gender=='m'or gender =='f':
			self.__gender = gender
		else:
			self.__gender = None			
			print "please print gender either as m or f"
