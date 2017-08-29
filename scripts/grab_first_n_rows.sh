#!/bin/bash

input_number=$1
number_lines=`echo "$input_number + 1" | bc`
shift

for file in "$@"
do
    filename=${file%.csv}
    output_file=${filename}_top_${input_number}.csv
    echo "$output_file"
    head -${number_lines} $file | tail -n+2 > $output_file
done
