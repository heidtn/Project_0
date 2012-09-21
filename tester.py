import sys
import scipy

import numpy
from numpy import *

import time


def main():
	i = 25
	for i in range(25):
		start = time.clock()
		stuff()
		end = time.clock()
		print end-start
		
def stuff():    #This is the function to test
	a = array([[1,2,3]])	
	print a
	
 
  
if __name__ == '__main__':
  main()


