#!/usr/bin/python

# Converts asn and org matchings in format found at (http://www.cidr-report.org/as2.0/autnums.html) to csv
# creates simple asn,org pair and removes all commas for organisation name

import io
import os.path
import sys

if len(sys.argv) != 2:
    print("Usage asn_to_org_converter.py [asn to org file]")
    exit(0)

asn_to_org_original = sys.argv[1]
asn_to_org_csv, ext = os.path.splitext(asn_to_org_original)
asn_to_org_csv += ".csv"
print("output: " + asn_to_org_csv)

with io.open(asn_to_org_csv, 'w') as out_file:
    with io.open(asn_to_org_original, 'r') as in_file:
        for line in in_file:
            line = line.rstrip('\n').encode('ascii', 'ignore')
            items = line.split(' ')
            asn = items[0][2:]
            org = ""
            for item in items:
                if item.startswith('AS'):
                    continue
                if item == " " or item == "":
                    continue
                if org == "":
                    org = item
                else:
                    org = org + " " + item
            org = org.replace(',', '')
            out_file.write(unicode(asn + "," + org + "\n"))

