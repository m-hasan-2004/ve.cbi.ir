import subprocess

def set_dns_windows(interface, server_ip):
    """
    Set the DNS server on Windows using PowerShell.

    Parameters:
    - interface (str): Network interface name (e.g., "Wi-Fi", "Ethernet").
    - server_ip (str): The IP address of the DNS server.

    Returns:
    - None
    """
    try:
        # Run PowerShell command to set DNS on Windows
        subprocess.run(["powershell", f"Set-DnsClientServerAddress -InterfaceAlias '{interface}' -ServerAddresses {server_ip}"])
        print(f"DNS set to {server_ip} on interface {interface}")
    except subprocess.CalledProcessError as e:
        print(f"Error setting DNS: {e}")

# Example usage on Windows
interface_name = 'Wi-Fi'  # Change this to your network interface name
dns_server_ip = '1.1.1.1'
set_dns_windows(interface_name, dns_server_ip)
