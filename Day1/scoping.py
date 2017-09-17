a = 6
print a, "outside fun"
d = 12
#_msg = 'Good Evening'  # __ makes it private
def fun():
	
	
	b = 9	
	
	a = 10	

	print a ,"inside fun"
  	print b

	global d #Avoid it

	d = 13 # d refers to the global d, 

	print d #13

	if a > 5 :
		x = "Good Afternoon"
	print x 

if __name__ == '__main__':
	fun()
	print d #13
	print a 

# this will give an error as we trying to print a value of a local variable
