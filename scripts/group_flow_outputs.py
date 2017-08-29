#!/usr/bin/python

from glob import glob
import io
from packet_out_stats import packet_out_stats, important_parts_of_csv
import sys

if len(sys.argv) != 3:
    print("Usage: group_flow_outputs.py [flow count files] [output file]")
    exit(0)

in_pattern = sys.argv[1]
output_file_name = sys.argv[2]
files = glob(in_pattern)
files.sort()
route_stats = []
ipocs = []
header = "/24_prefix,bgp_prefix,asn,org,packets_out_total,packets_out_total_%"

for filename in files:
    ipoc = important_parts_of_csv(filename)
    ipoc.add_routes_to_list(route_stats)
    ipocs.append(ipoc)

for ipoc in ipocs:
    header += "," + ipoc.capture_time + ",,"
    ipoc.add_stats_to_list(route_stats)

with io.open(output_file_name, 'w') as output_file:
    output_file.write(unicode(header + "\n"))
    for pos in route_stats:
        output_file.write(unicode(pos.get_as_csv() + "\n"))
