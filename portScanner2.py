import socket

commonPorts = {
    20: "FTP", 21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
    80: "HTTP", 110: "POP3", 443: "HTTPS", 3306: "MySQL", 8080: "HTTP Proxy", 8443: "HTTPS"
}
ports = list(commonPorts.keys())


def port_scan(target):
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Invalid target address.")
        return

    open_ports = []

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                open_ports.append(port)
                sock.close()
        except socket.error:
            pass

    return open_ports
