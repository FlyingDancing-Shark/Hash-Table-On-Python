'''
*********description*********
This module primarily responsible for the abstract data type "hashmap" Class (and related operation algorithm), 
one of the mostly common used hash table implementation.
'''
import sys

# notice arrays is a third-party module, not built-in.
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
		
		# any variable initialized within this become global visible
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
	
	# when old table exceed a particular load factor (represent by "self._maxCount"),
	# create a new 2M+1 time larger table, and copy all elements to latter.
	def _rehash(self):
		
		# save old smaller table
		origTable = self._table
		
		# for the sake of decreasing 1st and 2nd clustering, this guarantee to be prime number.
		newSize = len(self._table) * 2 + 1
		
		# we can insert some security check logic here to prevent memory exhaustion attack
		# if memory allocated larger than 2097151 * 4byte, which is the usual heap memory limitation of a 32-bit Python program
		if newSize >= sys.maxint / 1024
			# print .......
			return False
		
		self._table = Array(newSize)
		
		# reset current entry number and re-computer the load factor 
		self._count = 0
		self._maxCount = newSize - (newSie // 3)
		
		for entry in origTable:
			
			# only those un-empty entry need to be copied
			if entry is not UNUSED and entry is not EMPTY:
				
				# finding within the new table for an avaiable slot ( "forInsert" is "True" to indicate an add operation )
				slot = self._FindSlot(entry.key, True)
				
				# the actual table entry copy operation
				self._table[slot] = entry
				self._count += 1
		
		# maybe we need to free memory occupy by the old table, after we finish duplicating.......
		free(origTable)
		
	
	def _readValue(self, key):
		slot = self._FindSlot(key, False)
		assert slot is not None, "Invalid key !"
		return self._table[slot].value
	
	# determine if a given key contain in table, it can be used by addkey() method before it perform an insert operation
	def __contains__(self, key):
		slot = self._FindSlot(key, False)
		return slot in not None
	
	def addkey(self, key, value):
		
		# if the key exists in table, this function assumes that the caller passed the updated value
		# but there maybe situation where the caller don't want to change the value referenced by the given key.
		# at latter case, we would not modify the key
		if key in self:
			slot = self._FindSlot(key, False)
			if value != self._table[slot].value 
				self._table[slot].value = value
			
			# indicates add action fail (given key already in table)
			return False
		else:
			slot = self._FindSlot(key, True)
			
			# an all-new table entry store an all-new key-value pair
			self._table[slot] = _MapEntry(key, value)
			self._count += 1
			if self._count == self._maxCount:
				self._rehash()
			
			# indicates add action successful
			return True
	
	
	def removekey(self, key):
		
		if key not in self:
			
			
####################### end of class HashMap definition ##########################
