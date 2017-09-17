print 'Program starts'

n = raw_input('Enter n:')

try:
    a = int(n)

except ValueError:
     print 'Please enter an integer value'
# executes the below only when the corresponding try does not raise any exception
 
else:
     print a+2	   
 
print 'Program ends'
