class InvalidDaysError(Exception):
	def __init__(self,message):
		super(InvalidDaysError,self).__init__(message)
