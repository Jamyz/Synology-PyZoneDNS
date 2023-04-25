# Synology-DNS-IP-CHANGER
Changing DNS with Dynamic IPs

If your NS have a Dynamic IP. This python script replaces the line containing the old IP with the new one directly in DNS SERVER.

#This script gives for 2 different NS.

ns1.mydomain.com matches my1.dynamic.host
ns2.mydomain.com matches my2.dynamic.host
for mydomain.com, in the path /volume1/@appstore/DNSServer/named/etc/zone/master/mydomain.com

Once the IP has been changed in DNS SERVER, it restarts with the new IPs

#TaskManager
Create a TaskManager with root user. Put the desired periodicity (I recommend 1 hour minimum while the server restarts).
Add line script :
python3 /volume1/homes/User/PyZoneDNS.py
