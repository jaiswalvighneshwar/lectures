def fibo():
n = int(raw_input("Enter N: "))

a,b = 0,1
print a
print b

'''i = 2 using while loop
while i < n:
	c = a + b
	print c
	
	a,b= b, c
	i = i +1'''

# using For loop
for i in range(2, n):
	c = a+b
	print c	
	a,b=b,c



