class packet_out_stats:
    
    def __init__(self, s24_prefix, bgp_prefix, asn, org):
        self.s24_prefix = s24_prefix
        self.bgp_prefix = bgp_prefix
        self.asn = asn
        self.org = org
        self.stats = ""
        self.packets_out_total = 0
    
    def add_packet_out_stats(self, rule_number, packets_out, packets_out_percentage):
        self.stats += "," + rule_number + "," + packets_out + "," + packets_out_percentage # + ",=R[-1]+C[-1]"
        if packets_out != "":
            self.packets_out_total += int(packets_out)
        
    def get_as_csv(self):
        return self.s24_prefix + "," + self.bgp_prefix + "," + self.asn + "," + self.org + "," + str(self.packets_out_total) + "," + self.stats

import io

class important_parts_of_csv:
    
    def __init__(self, csv_file):
        self.data = dict()
        self.capture_time = csv_file.split('/')[-1].split('_')[0]
        with io.open(csv_file, 'r') as csv:
            rule_num = 0
            for line in csv:
                if line.startswith("/24_network"):
                    continue
                rule_num += 1
                line = line.rstrip('\n')
                items = line.split(',')
                self.data[items[0]] = (items[0], items[1], items[2], items[3], str(rule_num), items[7], items[10])
    
    def add_stats_to_list(self, route_list):
        for pos in route_list:
            if pos.s24_prefix in self.data:
                s24_prefix, bgp_prefix, asn, org, rule_num, packets_out, packets_out_percentage = self.data[pos.s24_prefix]
                pos.add_packet_out_stats(rule_num, packets_out, packets_out_percentage)
            else:
                pos.add_packet_out_stats("", "", "")
    
    def add_routes_to_list(self, route_list):
        if len(route_list) > 0:
            for prefix_key, data in self.data.items():
                s24_prefix, bgp_prefix, asn, org, rule_num, packets_out, packets_out_percentage = data
                if not check_if_prefix_in_list(s24_prefix, route_list):
                    route_list.append(packet_out_stats(s24_prefix, bgp_prefix, asn, org))
        else:
            for prefix_key, data in self.data.items():
                s24_prefix, bgp_prefix, asn, org, rule_num, packets_out, packets_out_percentage = data
                route_list.append(packet_out_stats(s24_prefix, bgp_prefix, asn, org))


def check_if_prefix_in_list(prefix, route_list):
    for pos in route_list:
        if prefix == pos.s24_prefix:
            return True
    return False
