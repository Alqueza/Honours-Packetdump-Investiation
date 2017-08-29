#!/usr/bin/python

from glob import glob
import io
import os.path
import subprocess
import sys

if len(sys.argv) != 3:
    print("Usage batch_convert_trace_to_flows.py [input trace(s) or directory] [output dir]")
    exit(0)

print("argument: " + sys.argv[1])

in_pattern = sys.argv[1]
output_dir = sys.argv[2]

for filename in glob(in_pattern):
    output_file_name = output_dir + filename.split('/')[-1]
    output_file_name, ext = os.path.splitext(output_file_name)
    output_file_name, ext = os.path.splitext(output_file_name)
    with io.open(output_file_name + ".flows", 'w') as output_file:
        subprocess.call(["/home/jwg13/bin/lpi_protoident", "-T", filename], stdout=output_file)

#print("The flow files are in \"" + output_dir + "\"")
