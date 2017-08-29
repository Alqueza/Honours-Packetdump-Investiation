
from network_instance import network_instance

from collections import defaultdict
import io
import os.path
from pyasn import pyasn, pyasn_radix
import sys
from timeit import default_timer as timer

def flow_counter(ipasn_db_file, flow_file, output_dir, asn_to_org):
    
    start_time = timer()
    
    #asn_to_org = dict()
    #with io.open(asn_to_org_file, 'r') as f:
    #    for line in f:
    #        line = line.rstrip('\n')
    #        items = line.split(',')
    #        asn_to_org[int(items[0])] = items[1]

    flow_file_name = flow_file.split('/')[-1]
    flow_file_name, ext = os.path.splitext(flow_file_name)
    output_file = output_dir + flow_file_name + "_flows_output.csv"
    all_output_file = output_dir + flow_file_name + "_flows_output_all.csv"

    #print("flow_counter:\tOutput file: " + output_file)
    #print("flow_counter:\tAll Outputs file: " + all_output_file)
    
    radix = pyasn(ipasn_db_file)
    flow_counts = dict()
    packets_out_sum = long(0)

    with io.open(all_output_file, 'w') as all_output:
        all_output.write(unicode("external_ip,network,asn,bytes_out,bytes_in,packets_out,packets_in\n"))
        with io.open(flow_file, 'r') as flows:
            for flow in flows:
                items = flow.split(' ')
                external_ip = items[2]
                asn, prefix = radix.lookup(external_ip)
                try:
                    org = asn_to_org[asn]
                except KeyError:
                    org = "Unknown"
                bytes_out = items[8]
                bytes_in = items[9]
                packets_out = items[10]
                packets_out_sum += long(packets_out)
                packets_in = items[11]
                if prefix in flow_counts:
                    flow_counts[prefix].add_data(bytes_out, bytes_in, packets_out, packets_in)
                else:
                    flow_counts[prefix] = network_instance(prefix, asn, org, bytes_out, bytes_in, packets_out, packets_in)
                all_output.write(unicode("{0},{1},{2},{3},{4},{5},{6},{7}\n".format(external_ip, prefix, asn, org.encode('utf-8'), bytes_out, bytes_in, packets_out, packets_in)))

    finished_processing_time = timer()
    print("flow_counter:\tPrinting results")

    with io.open(output_file, 'w') as output:
        output.write(unicode("network,asn,organisation,count,bytes_out,bytes_in,packets_out,packets_in,,packets_out_percentage\n"))
        for prefix, ni in flow_counts.items():
            percentage = float(ni.packets_out) / float(packets_out_sum) * 100
            output.write(unicode(ni.get_as_csv_line() + ",," + str(percentage) + "\n"))

    end_time = timer()

    print("flow_counter:\tProcessing time: " + str(finished_processing_time - start_time) + " (s)")
    #print("flow_counter:\tTotal time taken: " + str(end_time - start_time) + " (s)")
