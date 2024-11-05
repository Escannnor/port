import nmap  # Import the nmap library

def scan_ports(target_ip):
    """
    Scan the target IP for open ports using Nmap.

    :param target_ip: IP address to scan
    :return: Dictionary with open ports and detected services
    """
    nm = nmap.PortScanner()  # Initialize the Nmap PortScanner
    nm.scan(target_ip, '1-1024')  # Scan the first 1024 ports

    open_ports = {}

    for host in nm.all_hosts():
        print(f"Scanning Host: {host}")
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()  # Get the list of open ports for this protocol
            for port in lport:
                state = nm[host][proto][port]['state']
                if state == 'open':
                    service = nm[host][proto][port]['name']
                    version = nm[host][proto][port]['version']
                    open_ports[port] = {'service': service, 'version': version}
                    print(f"Port {port} is open and running {service} ({version})")
    return open_ports

if __name__ == "__main__":
    target_ip = input("Enter the target IP address (e.g., 192.168.1.1): ")
    open_ports = scan_ports(target_ip)
    print("Open Ports:", open_ports)
