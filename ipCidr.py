#!/usr/bin/python
#
# This script is used for CIDR conversion.
#
# Available auto-detected conversions are :
# - IP/Netmask to IP/CIDR
# - IP-Range to IP/CIDR
# - IP/CIDR to IP/Netmask
#
# Author: Emre Erkunt <emre.erkunt at gmail.com>
#
from netaddr import *
import sys
import re

# Auto-detect type of ARGV
regex = dict()
regex["ipNetmask"] = re.compile(r'(1[0-9][0-9]|2[0-4][0-9]|25[0-5]|[0-9][0-9]|[0-9])\.(1[0-9][0-9]|2[0-4][0-9]|25[0-5]|[0-9][0-9]|[0-9])\.(1[0-9][0-9]|2[0-4][0-9]|25[0-5]|[0-9][0-9]|[0-9])\.(1[0-9][0-9]|2[0-4][0-9]|25[0-5]|[0-9][0-9]|[0-9])\/(1[0-9][0-9]|2[0-4][0-9]|25[0-5]|[0-9][0-9]|[0-9])\.(1[0-9][0-9]|2[0-4][0-9]|25[0-5]|[0-9][0-9]|[0-9])\.(1[0-9][0-9]|2[0-4][0-9]|25[0-5]|[0-9][0-9]|[0-9])\.(1[0-9][0-9]|2[0-4][0-9]|25[0-5]|[0-9][0-9]|[0-9])')
regex["ipRange"] = re.compile(r'(1[0-9][0-9]|2[0-4][0-9]|25[0-5]|[0-9][0-9]|[0-9])\.(1[0-9][0-9]|2[0-4][0-9]|25[0-5]|[0-9][0-9]|[0-9])\.(1[0-9][0-9]|2[0-4][0-9]|25[0-5]|[0-9][0-9]|[0-9])\.(1[0-9][0-9]|2[0-4][0-9]|25[0-5]|[0-9][0-9]|[0-9])-(1[0-9][0-9]|2[0-4][0-9]|25[0-5]|[0-9][0-9]|[0-9])\.(1[0-9][0-9]|2[0-4][0-9]|25[0-5]|[0-9][0-9]|[0-9])\.(1[0-9][0-9]|2[0-4][0-9]|25[0-5]|[0-9][0-9]|[0-9])\.(1[0-9][0-9]|2[0-4][0-9]|25[0-5]|[0-9][0-9]|[0-9])')
regex["ipCidr"] = re.compile(r'(1[0-9][0-9]|2[0-4][0-9]|25[0-5]|[0-9][0-9]|[0-9])\.(1[0-9][0-9]|2[0-4][0-9]|25[0-5]|[0-9][0-9]|[0-9])\.(1[0-9][0-9]|2[0-4][0-9]|25[0-5]|[0-9][0-9]|[0-9])\.(1[0-9][0-9]|2[0-4][0-9]|25[0-5]|[0-9][0-9]|[0-9])\/(3[0-2]|2[0-9]|1[0-9]|[0-9])')

def usage():
    print "Usage: "+sys.argv[0]+" parameter"
    print "       IP/CIDR or IP/Netmask or IP-Range"
    sys.exit(1)

if ( len(sys.argv) < 2 ):
    usage()

match = regex["ipNetmask"].search(sys.argv[1])
if ( match is not None ):
    # IP Netmask to IP/CIDR conversion
    # print "Detected IP/Netmask"
    ip = IPNetwork(sys.argv[1])
    print str(ip.ip)+"/"+str(ip.prefixlen)+";"+str(ip.cidr)
else:
    match = regex["ipRange"].search(sys.argv[1])
    if ( match is not None ):
        # IP Range conversions
        # print "Detected IP-Range"
        rangeStart = match.group(1)+"."+match.group(2)+"."+match.group(3)+"."+match.group(4)
        rangeEnd = match.group(5)+"."+match.group(6)+"."+match.group(7)+"."+match.group(8)
        ipRange = IPRange(rangeStart, rangeEnd)
        for cidr in ipRange.cidrs():
            print cidr
    else:
        match = regex["ipCidr"].search(sys.argv[1])
        if ( match is not None ):
            # IP/Cidr conversions
            if ( int(sys.argv[1].split("/")[1]) > 32 ):
                usage()
            ip = IPNetwork(sys.argv[1])
            print str(ip.ip)+"/"+str(ip.netmask)
        else:
            print sys.argv[1]+" does not meet any criteria ( IP/CIDR, IP/Netmask, IP-Range )"
            sys.exit(1)

sys.exit(0)
