# PortScanner: A simple TCP port scanner that uses the 'socket' library to scan for open ports on a target machine.

import socket

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

for port in range(1, 100):
    scan(targetIp, port)

print("Scan complete!")