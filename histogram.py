'''
*********description*********
this Class implement the abstract data structure "histogram", which make use of "HashMap" hash table for store 
and query statistical related information.
'''

from hashmap import HashMap, _MapEntry

class Histogram:

	# "catSeq" represent a particular sequence of category identifier.
	def __init__(self, catSeq):
		
		# Histogram.frequenceCounts , is actually a hash table
		self._frequenceCounts = HashMap()
		
		for category in catSeq:
			
			# so it has a addkey() method, here "category" is single character-based key, "0" is value
			# the letter with uppercase will be hash to integer-based key
			# and a empty slot will be fill with new key-value(0) pair entry
			# the value(0) represent the initialized counter=0 for each category
			self._frequenceCounts.addkey(category, 0)
			
