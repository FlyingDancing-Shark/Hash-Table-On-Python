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
		
		for L_category in catSeq:
			
			# so it has a addkey() method, here "category" is single character-based key, "0" is value
			# the letter-based key with uppercase will be hash to integer-based key
			# and a empty slot will be fill with new entry, that is,
			# key-value(0) pair 
			# the value(0) represent the initialized counter=0 for each category
			self._frequenceCounts.addkey(L_category, 0)
	
	def getCount(self, category):
		
		# determine if key in hash table
		assert category in self._frequenceCounts, "Invalid histogram category !"
		return self._frequenceCounts._readValue(category)
	
	def increaseCount(self, category):
		
		# determine if key in hash table
		assert category in self._frequenceCounts, "Invalid histogram category !"
		value = self._frequenceCounts._readValue(category)
		
		# in the main() function of buildHistogram.py, 
		# each time we achieve a data belongs to particular category, 
		# add corresponding counter value by one
		self._frequenceCounts.addkey(category, value + 1)
		
	def totalCount(self):
		total = 0
		for L_category in self._frequenceCounts:
			total += self._frequenceCounts._readValue(category)
		return total
	
	# returns an iterator for traversing the categories.
	def __iter__(self):
		return iter(self._frequenceCounts)
	
	
		
