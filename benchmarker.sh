#!/bin/bash


for(( i = 0; i < 10; i ++  ))
do

NUMBER=$i
# touch /testfiles/testfile$NUMBER.txt
python gen-valid.py $NUMBER > testfiles/testfile$NUMBER.txt

done
