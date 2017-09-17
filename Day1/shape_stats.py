class Shape(object):  #define a method class to add strict checks so that they are 

	def area(self):
		pass
	def perimeter(self):
		pass
		

class ShapeStatistics(object):
	
	@staticmethod    # this is a decorator. it is used to  disiinguish it is as a class method
	def get_stats(shape):
		if isinstance(shape, Shape):			
			a = shape.area()
			p = shape.perimeter()
			return 'Area : {0}\nPerimeter: {1}'.format(a, p)	
		    
	    	else:
			print 'Please pass something which is from class Shape'
