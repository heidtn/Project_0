from numpy import *
import re
class IOException(Exception):
        pass
class InputFormatError(IOException):
        def __init__ (self, line, str):
                print "Input Format Error, Bad input"
		print str

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
        except ValueError:
                raise InputFormatError(line, "Input Format Error: Bad Input")
                sys.exit()

# automagically splits the whole array into A and b
A, b =  hsplit(array(arr), [len(arr[0]) - 1])

try:
	x = dot(linalg.pinv(A), b)
except Exception:
	raise InputFormatError(A, "improperly sized array")	

for i in x:
        print("%6.3e" % i[0])
