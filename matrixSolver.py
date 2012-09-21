from numpy import *
import re

line = '0'
arr = []

while(line != ''):
	#gets input
        line = raw_input('enter line\n')
	
	#if reached EOF marker
        if(not line): break

	# fancy list comprehension.  Allows spaces and ; at the end of a line
        arr.append([float(x) for x in line.split(';') if x != ''])


# automagically splits the whole array into A and b
A, b =  hsplit(array(arr), [len(arr[0]) - 1])


# temporary debug lines
print A
print '\n\n'
print b
print '\n\n'

x = dot(linalg.pinv(A), b)
print x


