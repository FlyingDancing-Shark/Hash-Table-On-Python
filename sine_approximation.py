'''
*********description*********

'''

import math

x_for_sine = 7
max_power = 30
counter = 1
sum = x_for_sine
sign = 1.0

while counter < max_power :
	
	sign = -sign
	counter += 2
	trem = sign*x_for_sine**counter / math.factorial(counter)
	sum += trem

# this print syntax only legitimate for Python 2.X ,for Python 3.x , using print()	
print 'sin(%g) = %.32f (approximation with %d terms)' % (x_for_sine, sum, max_power) 
  
