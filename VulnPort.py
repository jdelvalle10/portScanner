from portScanner2 import port_scan

target_website = input("[+] Enter target website in format 'www.example.com': ")

open_ports = port_scan(target_website)
if open_ports:
    print("Open ports on {}: {}".format(target_website, open_ports))
else:
    print("No open ports found on {}.".format(target_website))
