#!/bin/bash

for(( i = 3; i < 300; i ++  ))
do

NUMBER=$i

echo -n "$NUMBER," >> timeresults/timeresult.txt

/usr/bin/time -f "%E real,%U user,%S system\n" -a -o timeresults/timeresult.txt python matrixSolver.py < testfiles/testfile$NUMBER.txt > testresults/soln$NUMBER.txt

done
