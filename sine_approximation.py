'''
*********description*********

'''

import math

x_for_sine = 7
max_power = 30
counter = 1
sum = x_for_sine
sign = 1.0
term_table = []

while counter < max_power :
	
	sign = -sign
	counter += 2
	trem = sign*x_for_sine**counter / math.factorial(counter)
	sum += trem
	term_table.append(trem)

exponential_table = [ exp_term*10**6 for exp_term in term_table ]
	
# this print syntax only legitimate for Python 2.X ,for Python 3.x , using print()	
print '\n\nsin(%g) = %.32f (approximation with %d terms)' % (x_for_sine, sum, max_power) 

print '\nthose terms we used for calculate the approximation of sin(%g) are:\n' \
	% (x_for_sine) 

"""
for term in term_table:
	print term
"""

for ori_term, exp_term in zip(term_table, exponential_table): 
	print '%.16f 	%.16f-----exponentiation by 10^6-----' % (ori_term, exp_term)

	
	
