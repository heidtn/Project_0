from numpy import *
import re

line = '0'
arr = []

while(line != ''):
	#gets input
	try:
        	line = raw_input()
	except EOFError:
		break
		
	#if reached EOF marker
        if not line: break
	line = line.strip()
	
	# fancy list comprehension.  Allows spaces and ; at the end of a line
	try:
		arr.append([float(x) for x in line.split(';') if x != ''])
	except InputFormatError:
		print "Invalid input cannot be parsed"

# automagically splits the whole array into A and b
A, b =  hsplit(array(arr), [len(arr[0]) - 1])


# temporary debug lines 
x = dot(linalg.pinv(A), b)
for i in x:
	print str(i).format("%6.3e")

#class InputFormatError(Exception)
#	def __init__ (self, expr, msg):
#		self.expr = expr
#		self.msg = msg
