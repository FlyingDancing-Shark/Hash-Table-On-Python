'''
*********description*********
this main program make use of histogram class and underlying hash table implementation, 
read a collection of data from a text file, 
and generate a statistics chart(occurrence frequency)  for it.
'''

from histogram import Histogram

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
	
	print("			Grade Distribution")
	
	grades = ('A', 'B', 'C', 'D', 'E', 'F')
	for letter in grades:
		print("    |")
		print(letter + " +", end = "")
		count = instanceHist.getCount(letter)
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
	
	gen_chart(instanceHistogram)	


main()


