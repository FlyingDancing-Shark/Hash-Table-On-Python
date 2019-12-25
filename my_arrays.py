'''
*********description*********
note that we distinguish  this module from the Python build-in "array" module 
by putting a "my_" sperfix and an "s" suffix on its name.
'''

import ctypes

class Array:
	
	def clear(self, value):
		for i in range(len(self)):
			self._elements[i] = value
	
	
	def __init__(self, size):
		assert size > 0, "Array size must be larger than 0"
		self._size = size
		
		PyArrayType = ctypes.py_object * size
		self._elements = PyArrayType()
		self.clear(None)
		
	def __len__(self):
		return self._size
	
	def __getitem__(self, index):
		assert index >= 0 and index < len(self), "Array subscript out of range"
		return self._elements[index]
	
	def __setitem__(self, index, value):
		assert index >= 0 and index < len(self), "Array subscript out of range"
		self._elements[index] = value
		
	def __iter__(self):
		return _ArrayIterator(self._elements)

	"""note than in Python 2.x, syntax :
		for <some element> in Array instance 
	didn't work, instead, we shuould use syntax :
		for i in range(len(Array instance))
	"""
	
				
class _ArrayIterator:
	
	def __init__(self, theArray):
		self._arrayReference = theArray
		self._curNdx = 0
		
	def __iter__(self):
		return self
	
	def __next__(self):
		if self._curNdx < len(self._arrayReference):
			entry = self._arrayReference[self._curNdx]
			self._curNdx += 1
			return entry
		else:
			raise StopIteration
			
			
