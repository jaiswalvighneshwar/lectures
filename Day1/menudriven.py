while True :
	print '1. Fibo Series'
	print '2. Even Series'
	print '3. Even or Odd'
	print '4. Exit'

	choice = int(raw_input("Enter your choice: "))
	
	if choice != 4:
		n = input('Enter n:')
	if choice == 1:
		a,b = 0,1
		print a
		print b

		for i in range(2, n):
			c = a+b
			print c	
			a,b=b,c

	elif choice == 2: 
		for i in range(0, n+1, 2):
			print i

	elif choice == 3:
		if n % 2 == 0:
			print str(n) + " is even"
		else:
			print str(n) + " is odd"

	else:
		break
