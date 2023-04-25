# coding=utf-8
import socket
import os

# Resolve IP address for my.dynamic.host
try:
    myhost_ip = socket.gethostbyname('my.dynamic.host')
except socket.gaierror:
    print('Error: Unable to resolve the IP address for my.dynamic.host.')
    exit()

# Resolve IP address for my2.dynamic.host
try:
    myhost2_ip = socket.gethostbyname('my2.dynamic.host')
except socket.gaierror:
    print('Error: Unable to resolve the IP address for my2.dynamic.host.')
    exit()

# Check if my.dynamic.host is responding
try:
    socket.create_connection((myhost_ip, 80), timeout=1)
except socket.error:
    print('my.dynamic.host do not answer.')
else:
    # Ouvrir le fichier de zone DNS et le lire en mémoire
    with open('/volume1/@appstore/DNSServer/named/etc/zone/master/mydomain.com', 'r') as f:
        lines = f.readlines()

    # Open the DNS zone file and read it into memory
    for i, line in enumerate(lines):
        # Find the line containing the IP address for ns2.mydomain.com
        if 'ns2.mydomain.com.\t86400\tA' in line:
            ns2_ip_address = line.split()[-1]
            # Compare IP addresses
            if myhost_ip != ns2_ip_address:
                print('The IP addresses for ns2.mydomain.com are different:')
                print(' - my.dynamic.host : {}'.format(myhost_ip))
                print(' - ns2.mydomain.com : {}'.format(ns2_ip_address))

                # Edit line in DNS zone file for ns2.mydomain.com
                lines[i] = 'ns2.mydomain.com.\t86400\tA\t{}\n'.format(myhost_ip)

                # Write changes to DNS zone file
                with open('/volume1/@appstore/DNSServer/named/etc/zone/master/mydomain.com', 'w') as f:
                    f.writelines(lines)

                # Restart the DNS Server service
                os.system('synoservice --restart pkgctl-DNSServer')
                print('The DNS Server service is restarted...')
                print('The IP addresses have been changed successfully.')
                break

            else:
                print('The IP addresses for ns2.mydomain.com are identical:', myhost_ip)

# Check if my2.dynamic.host is responding
try:
    socket.create_connection((myhost2_ip, 80), timeout=1)
except socket.error:
    print('my2.dynamic.host do not answer.')
else:
    # Open the DNS zone file and read it into memory
    with open('/volume1/@appstore/DNSServer/named/etc/zone/master/mydomain.com', 'r') as f:
        lines = f.readlines()

    # Go through each line of the DNS zone file
    for i, line in enumerate(lines):
        # Find the line containing the IP address for ns1.mydomain.com
        if 'ns1.mydomain.com.\t86400\tA' in line:
            ns1_ip_address = line.split()[-1]
            # Compare IP addresses
            if myhost2_ip != ns1_ip_address:
                print('The IP addresses for ns1.mydomain.com are different:')
                print(' - my2.dynamic.host : {}'.format(myhost2_ip))
                print(' - ns1.mydomain.com : {}'.format(ns1_ip_address))

                # Edit line in DNS zone file for ns1.mydomain.com
                lines[i] = 'ns1.mydomain.com.\t86400\tA\t{}\n'.format(myhost2_ip)

                # Write changes to DNS zone file
                with open('/volume1/@appstore/DNSServer/named/etc/zone/master/mydomain.com', 'w') as f:
                    f.writelines(lines)

                # Restart the DNS Server service
                os.system('synoservice --restart pkgctl-DNSServer')
                print('The DNS Server service is restarted...')
                print('The IP addresses have been changed successfully.')
                break

            else:
                print('The IP addresses for ns1.mydomain.com are identical:', myhost2_ip)
