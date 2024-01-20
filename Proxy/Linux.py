import subprocess

def set_dns_linux(interface, server_ip):
    """
    Set the DNS server on Linux.

    Parameters:
    - interface (str): Network interface name (e.g., "eth0", "wlan0").
    - server_ip (str): The IP address of the DNS server.

    Returns:
    - None
    """
    try:
        # Run the system command to set DNS on Linux
        subprocess.run(["sudo", "nmcli", "dev", "modify", interface, "ipv4.dns", server_ip])
        subprocess.run(["sudo", "nmcli", "dev", "modify", interface, "ipv6.dns", server_ip])
        print(f"DNS set to {server_ip} on interface {interface}")
    except subprocess.CalledProcessError as e:
        print(f"Error setting DNS: {e}")

# Example usage on Linux
interface_name = 'wlp2s0'  # Change this to your network interface name
dns_server_ip = '1.1.1.1'
set_dns_linux(interface_name, dns_server_ip)
