# honours-packet-trace-investiation

This contains the various scripts I used to get the statistics of packets leaving the Waikato Network, this information was used to determine the percentage of packets that get hit by routes in the BGP RIB.

Packet traces were decoded into flows using the lpi_protoident tool (https://github.com/wanduow/libprotoident).
A BGP RIB from sydney (http://routeviews.org/route-views.sydney/bgpdata/) was imported using the pyasn package.
The external ip address, number of packets and number of bytes were taken from the flows and grouped by BGP routes.
This information was used to see how many routes were used to route x% of packets and the size a route cache would need to be to be able to route efficiently.
