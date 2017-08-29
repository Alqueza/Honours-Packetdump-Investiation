#!/usr/bin/python

from flow_counter import flow_counter

from glob import glob
import io
import os.path
import sys


if len(sys.argv) != 5:
    print("Usage flow_counter.py [ipasn db file] [flows] [output dir] [asn to org file]")
    exit(0)

ipasn_db_file = sys.argv[1]
flows_pattern = sys.argv[2]
output_dir = sys.argv[3]
asn_to_org_file = sys.argv[4]

if not os.path.isdir(output_dir):
    print(output_dir + " is not a valid directory")
    exit(0)
    
asn_to_org = dict()
with io.open(asn_to_org_file, 'r') as f:
    for line in f:
        line = line.rstrip('\n')
        items = line.split(',')
        asn_to_org[int(items[0])] = items[1]

files = glob(flows_pattern)
number_of_files = len(files)
number_of_files_processed = 0

for filename in files:
    number_of_files_processed +=1
    print("Processing " + filename + "," + str(number_of_files_processed) + " file(s) processed, " + str(number_of_files - number_of_files_processed) + " left")
    flow_counter(ipasn_db_file, filename, output_dir, asn_to_org)
    
