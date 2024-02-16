import socket


def port_scan(target):
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Invalid target address.")
        return

    open_ports = []

    for port in range(1, 100):
        try:
            sock = socket.socket()
            sock.settimeout(0.5)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                open_ports.append(port)
                sock.close()
        except socket.error:
            pass
    return open_ports


def banner_grabber(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(4096)
        return banner
    except:
        return
