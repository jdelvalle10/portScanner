# PortScanner to find vulnerable ports, using nmap.
# Author: Jose Luis Del Valle

# First, we need to install the nmap library.
import nmap

# Now we prompt the user to enter the target website.
target = input('[+] Enter the target website in format www.example.com: ')

# First, we need to create a PortScanner object.
nm = nmap.PortScanner()
# Now we set the range of ports we want to scan.
nm.scan(target, '21-443')
# Finally, we print the results.
print(nm.csv())


# Let's print out the services that are running on the open ports.
for host in nm.all_hosts():
    print('Host: %s (%s)' % (host, nm[host].hostname()))
    print('State: %s' % nm[host].state())
    for proto in nm[host].all_protocols():
        print('Protocol: %s' % proto)
        lport = nm[host][proto].keys()
        for port in lport:
            print('port: %s\tstate: %s' % (port, nm[host][proto][port]['state']))
            print('service: %s' % nm[host][proto][port]['name'])
            print('product: %s' % nm[host][proto][port]['product'])
            print('version: %s' % nm[host][proto][port]['version'])
            print('extrainfo: %s' % nm[host][proto][port]['extrainfo'])
            print('reason: %s' % nm[host][proto][port]['reason'])
            print('cpe: %s' % nm[host][proto][port]['cpe'])
            print('conf: %s' % nm[host][proto][port]['conf'])

# Now we export the results to a csv file.
with open('vulnerablePorts.csv', 'w') as f:
    f.write(nm.csv())
    f.close()
# Done!

# These are other useful methods of the PortScanner class:
# nm.all_hosts() -> returns a list of all the hosts that were scanned.
# nm.scaninfo() -> returns a dictionary with the scan information.
# nm.scanstats() -> returns a dictionary with the scan statistics.
# nm.all_protocols() -> returns a list of all the protocols that were scanned.
# nm[host] -> returns a dictionary with the scan results of the specified host.
# nm.csv() -> returns a string with the scan results in csv format.

# Now that we know the ports that are open, we can use the nmap library to find out if they are vulnerable.
# We can use the nmap library to scan for vulnerabilities in the open ports.
# This is an example of how to use the nmap library to scan for vulnerabilities in the open ports.
