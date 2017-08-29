#!/usr/bin/python

import io
import sys

if len(sys.argv) != 2:
    print("Usage get_all_nones_from_flow_counts.py [flow counts all file]")
    exit(0)

with io.open(sys.argv[1], 'r') as flow_count_file:
    for line in flow_count_file:
        line = line.rstrip('\n')
        items = line.encode('ascii', 'ignore').split(',')
        if items[1] == "None":
           print(line)
