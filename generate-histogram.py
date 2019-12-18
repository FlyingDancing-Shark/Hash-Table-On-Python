'''
*********description*********
this main program make use of histogram class and underlying hash table implementation, 
read a collection of data from a text file, 
and generate a statistics chart(occurrence frequency)  for it.
'''

from histogram import Histogram

# receive a two-digits-based integer "score" as parameter
def scoreToLetterGrade(score):
	
	if score >= 90 :
 		return 'A'
	elif score >= 80 :
		return 'B'
	elif score >= 70 :
 		return 'C'
 	elif score >= 60 :
 		return 'D'
 	else :
 		return 'F'
		
	
def gen_chart(instanceHist):
	
	# indent to arrange this message right in the middle of the chart top
	print("			Grade Distribution")
	
	# a set of hash keys use for query operation
	grades = ('A', 'B', 'C', 'D', 'E', 'F')
	for letter in grades:
		print("    |")
		print(letter + " +", end = "")
		
		# here, individual "key" act as an index into hash table to get corresponding "value" 
		# (count for that "key" category)
		count = instanceHist.getCount(letter)
		
		# multiply single asterisk by number we get multiple asterisk that visually represent 
		# the appear frequency of a specific letter grade category 
		print("*" * count)
	
	print("    |")
	print( " +-----+-----+-----+-----+-----+-----+-----+-----" )
	print( " 0     5     10    15    20    25    30    35" )


def main():
	
	instanceHistogram = Histogram("ABCDF")
	dataset = open('score_transcript.txt', "r")
	
	for each_line in dataset:
		letter_grade = scoreToLetterGrade(int(each_line))
		instanceHistogram.increaseCount(letter_grade)
		
	# when for loop exit, the five category have finished their statistic, ready for subsequently display
	gen_chart(instanceHistogram)	


# drive the main working process
main()

