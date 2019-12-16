'''
description

'''

from arrays import Array

class _MapEntry:
	def __init__(self, key, value):
		self.key = key
		self.value = value


class HashMap:
	
	# this represent a null reference within the table, not occupy by any table entry.
	UNUSED = None
	# this create an empty table entry with no key and value, used to compare in the subsquent logic
	# if we remove a previously existing entry, we can use this dummy EMPTY entry to flag the removed status and distinguish from an really empty (UNUSED) that  never use before.
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
	
	def _FindSlot(self, key, forInsert):
		
		# compute the key's original hash 
		slot = self._hash1(key)
		
		# when we encounter a null reference in table, the loop and method exit with no return value ( indicate None ), 
		# can use by caller (e.g., __contains__ )to determine whether a given key exist in table.
		while self._table[slot] is not UNUSED:
			
			# when caller want to find a empty slot to add new key, we give it one that meets requirement.
			if forInsert and (self._table[slot] is UNUSED or self._table[slot] is EMPTY):
				return slot
			
			# when caller want to check the existence of a given key, 
			# we search for those un-empty entry, and compare their "key" attribute to the given one.
			elif not forInsert and (self._table[slot] is not EMPTY and self._table[slot].key == key):
				return slot
			
			# if caller want to add new key, but the original slot was occupied by another 
			# key (hash collision), we use 2nd hash function to compute new slot to check.
			else:
				step_size = self._hash2(key)
				M = len(self._table)
				
				slot = (slot + step_size) % M
				
	
	def _readValue(self, key):
		slot = _FindSlot(key, False)
		assert slot is not None, "Invalid key !"
		return self._table[slot].value
	
	
