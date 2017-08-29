#!/bin/bash

# batch sort flow_count files keeping the header intact
# arguments can be 
#       example/example1.csv
#       example/example1.csv example/example2.csv etc.
#       example/*.csv

for file in "$@"
do
    echo "Sorting $file"
    filename=${file%.csv}
    output_file=${filename}_sorted.csv
    echo "Output ${output_file}"
    head -1 $file > $output_file
    tail -n+2 $file | sort -nrt ',' -k 8,8 >> $output_file
done
