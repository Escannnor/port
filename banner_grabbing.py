import socket

def grab_banner(ip, port):
    """
    Grab the service banner running on a given IP and port.

    :param ip: Target IP address
    :param port: Target port number
    :return: Service banner (if available)
    """
    try:
        s = socket.socket()
        s.settimeout(3)
        s.connect((ip, port))
        banner = s.recv(1024).decode().strip()
        s.close()
        return banner
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    ip = input("Enter the IP address (e.g., 192.168.1.1): ")
    port = int(input("Enter the port number (e.g., 22): "))
    banner = grab_banner(ip, port)
    print(f"Service Banner: {banner}")
