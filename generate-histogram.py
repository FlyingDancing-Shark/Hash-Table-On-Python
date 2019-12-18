'''
*********description*********
this main program make use of histogram class and underlying hash table implementation, 
read a collection of data from a text file, 
and generate a statistics chart(occurrence frequency)  for it.
'''

from histogram import Histogram

def scoreToLetterGrade(score):
	
	if score <=:
		return 
	elif score <=:
		
	elif score <=:
		
	elif score <=:
		
	
def gen_chart():
	
	print(				"distribution")
	
	grade = ("A", "B", "C", "D", "E", "F")
	for letter in grade:
		count = instanceHistogram.getCount(letter)
		print(letter + )
		print("*" * count)
	
	
	print(				"+")
	print(				"------------------")
	print(				"")

	
def main():
	
	instanceHistogram = Histogram("ABCDEF")
	dataset = open("score_transcript.txt", r)
	
	for each_line in dataset:
		
		letter_grade = scoreToLetterGrade(int(score))
		instanceHistogram.increaseCount(letter_grade)
	
	gen_chart(instanceHistogram)	
	
  
main()



