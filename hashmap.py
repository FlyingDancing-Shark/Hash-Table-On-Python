'''
description

'''

from arrays import Array

class _MapEntry:
	def __init__(self, key, value):
		self.key = key
		self.value = value


class HashMap:
	
	UNUSED = None
	# this create an empty table entry with no key and value, used to compare in the subsquent logic
	EMPTY = _MapEntry(None, None)
	
	def __init__(self):
		self._table = Array(7)
		# currently amount of key store in the table
		self._count = 0
		# equivalent to load factor = 2/3
		self._maxCount = len(self._table) - len(self._table) // 3
		# Returns the number of entries in the map.
	def __len__(self):
		return self._count
	
	def _hash1(self, key):
		# hash() used for handle the possible string type key, and abs() always returen positive value. 
		return abs(hash(key)) % len(self._table)
	
	def _hash2(self, key):
		return 1 + abs(hash(key)) % (len(self._table) - 2)
	
	
	
