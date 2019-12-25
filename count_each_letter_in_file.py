'''
*********description*********
this program actually count the number of occurrences of each letter in a text file.
'''

from array import Array

chrCounter = Array(127)
chrCounter.clear(0)

txtFile = open('testFile.txt', 'r')
for line in txtFile:
	for letter in line:
    	ascii_code = ord(letter)
    	chrCounter[ascii_code] += 1
		
txtFile.close()

for i in range(26):
	print( "%c - %4d                %c - %4d" % \
			(chr(65+i), chrCounter[65+i], chr(97+i), chrCounter[97+i]) )
