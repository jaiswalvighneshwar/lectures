#import series

from series import fibo as fi ,evenseries as es

import xyz.supercoders.math as mo
import math
import scoping

print math.pi
print scoping.a
# print scoping.msg

while True :
	print '1. Fibo Series'
	print '2. Even Series'
	print '3. Even or Odd'
	print '4. Exit'

	choice = int(raw_input("Enter your choice: "))
	
	if choice != 4:
		n = input('Enter n:')
	if choice == 1:
		print fi(n)
	elif choice == 2:
		print es(n)
	elif choice == 3:
		if mo.iseven(n):
			print str(n) +" is even"
		else :
			print str(n) +"is Odd"
	else:	
		break
