# ipCidr (https://api.travis-ci.org/eerkunt/ipCidr.svg)

This script converts
* IP/Netmask to IP/CIDR
* IP/CIDR to IP/Netmask
* IP-Range to IP/CIDR(s)

# Examples

IP/Netmask to IP/CIDR Conversion :
```
$ ./ipCidr.py 192.168.0.1/255.255.255.0
192.168.0.1/24;192.168.0.0/24
```

IP/CIDR to IP/Netmask Conversion :
```
$ ./ipCidr.py 192.168.0.0/24
192.168.0.0/255.255.255.0
$ ./ipCidr.py 192.168.0.1/24
192.168.0.1/255.255.255.0
```

IP-Range to IP/CIDR(s) Conversion :
```
$ ./ipCidr.py 192.168.0.0-192.168.0.255
192.168.0.0/24

$ ./ipCidr.py 192.168.0.1-192.168.0.255
192.168.0.1/32
192.168.0.2/31
192.168.0.4/30
192.168.0.8/29
192.168.0.16/28
192.168.0.32/27
192.168.0.64/26
192.168.0.128/25
```
