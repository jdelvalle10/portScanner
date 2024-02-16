from portScanner2 import *

target_website = input("[+] Enter target website in format 'www.example.com': ")

open_ports = port_scan(target_website)

if open_ports:
    for p in open_ports:
        target_ip = socket.gethostbyname(target_website)
        b = banner_grabber(target_ip, p)
        print(f"Open port {p} in {target_ip} is running {b}")
else:
    print(f"No open ports found on {target_website}.")
