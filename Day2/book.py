class Book:
	

	def __init__(self,title,pages,price,authors=None):
		self.title = title
		self.pages = pages
		self.price = price
		self.authors = authors

	def has_authors(self):
		if self.authors:
			return True
		return False

	def get_details(self):
		details = "Title: {0}\nPages: {1}\nPrice: {2}".format(self.title,self.pages,self.price)
		
		if self.has_authors():
			for auth in self.authors:
				details = details + '\n' + auth.get_details()
		return details
