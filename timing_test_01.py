import sys

#time module import for performance testing
import time



def main():
  
  #take arg after filename at runtime
  x = int(sys.argv[1])
  
  #set start time
  starttime = time.time()
  
  #run repeater recursive fn to test (997 is the max for my machine, for whatever reason)-MD
  repeater(x)
  
  #mark end time
  endtime = time.time()
  
  #calc elapsed and put into minute form, just because
  elapsedtime = endtime - starttime
  mintime = elapsedtime/60
  #print time elapsed
  print "Time elapsed:", elapsedtime, "seconds, which is:", mintime, "minutes"


def repeater(x):
  print x
  x = x - 1
  if x >= 0:
    return repeater(x)
  else:
    return

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

  
#timing code from:http://web.archive.org/web/20100825233709/http://www.techarticles.zeromu.net/programming/keeping-track-of-elapsed-time-in-python/
  
  