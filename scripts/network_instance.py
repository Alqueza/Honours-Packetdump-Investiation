class network_instance:
    
    def __init__(self, prefix, asn, org, bytes_out, bytes_in, packets_out, packets_in):
        self.prefix = prefix
        self.asn = asn
        self.org = org
        self.count = 1
        self.bytes_out = long(bytes_out)
        self.bytes_in = long(bytes_in)
        self.packets_out = long(packets_out)
        self.packets_in = long(packets_in)
        self.packets_out_percentage = long(0)
    
    def add_data(self, bytes_out, bytes_in, packets_out, packets_in):
        self.count += 1
        self.bytes_out += long(bytes_out)
        self.bytes_in += long(bytes_in)
        self.packets_out += long(packets_out)
        self.packets_in += long(packets_in)

    def get_as_csv_line(self):
        return "{0},{1},{2},{3},{4},{5},{6},{7}".format(
                self.prefix, 
                self.asn, 
                self.org,
                self.count, 
                self.bytes_out, 
                self.bytes_in,
                self.packets_out,
                self.packets_in)
    
