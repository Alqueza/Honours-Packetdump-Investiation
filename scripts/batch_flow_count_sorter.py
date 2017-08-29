#!/usr/bin/python

from glob import glob
import io
import subprocess
import sys

if len(sys.argv) != 3:
    print("Usage batch_flow_count_sorter.py [input file(s) or directory] [output dir]")
    exit(0)

print("argument: " + sys.argv[1])

in_pattern = sys.argv[1]
output_dir = sys.argv[2]

for filename in glob(in_pattern):
    
    print(output_dir + filename.split('/')[-1] + "_sorted.csv")
    
    
    
    
    
    #sort_cmd = "sort -nrt ',' -k 7,7 " + filename
    #print(sort_cmd)
    #with io.open(output_dir + filename.split('/')[-1] + "_sorted.csv", 'w') as output_file:
    #    subprocess.call(["sort -nrt ',' -k 7,7 " + filename], stdout=output_file)

# -nrt ',' -k 7,7
#sort -n -r -t ',' -k 7,7
#sort -nrt ',' -k 7,7 
#ls *_output.csv | xargs -i% -n1 sort -nrt ',' -k 7,7 % -o %.sorted
