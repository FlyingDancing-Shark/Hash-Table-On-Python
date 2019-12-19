'''
*********description*********

'''

import math

max_power = 7
counter = 1
x_for_sine = 7
sign = 1.0
sum = x_for_sine

while counter < 7 :
	
	sign = -sign
	counter += 2
	trem = sign*x_for_sine**counter / math.factorial(counter)
	sum += trem

print "sin(%g) = %g (approximation with %d terms)" % (x_for_sine, sum, max_power) 	
  

