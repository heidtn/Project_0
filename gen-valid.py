from numpy import *
from pylab import *
from sys import stdout, stderr

N = randint(250)
X = randn(N,N+1)

for r,row in enumerate(X):
  for c,val in enumerate(row):
    fmt = "%%%d.%d%s" % ( randint(3,15), randint(0,8), "efg"[randint(3)] )
    stdout.write( fmt % val )
    if randint(10)==0:
      delim = "\t"*int(4*rand()**3)+";"+" "*int(10*rand()**3)    
    else:
      delim = " "*int(10*rand()**3)+";"+" "*int(10*rand()**3)    
    if c==N:
      stdout.write( "\n" if randint(5)>0 else delim+"\n" )
    else:
      stdout.write( delim )

stderr.write("valid N=%d\n" % N)
