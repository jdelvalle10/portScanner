# PortScanner: A simple TCP port scanner that uses the 'socket' library to scan for open ports on a target machine.

import socket

# Define a dictionary of common ports and their services
commonPorts = {20:"FTP", 21:"FTP", 22:"SSH", 23:"Telnet", 25:"SMTP", 53:"DNS", 80:"HTTP", 110:"POP3", 443:"HTTPS", 3306:"MySQL", 8080:"HTTP Proxy", 8443:"HTTPS"}
ports = list(commonPorts.keys())


def scan(t, p):
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((t, p))
        b = sock.recv(1024)
        print(f"Port {p} is open on {t} with banner: {b}")
    except:
        pass
    finally:
        sock.close()

target = input("[+] Enter target website in format 'www.example.com': ")
targetIp = socket.gethostbyname(target)

for port in ports:
    scan(targetIp, port)

print("Scan complete!")

