import subprocess

def ping_server(ip_address):
    try:
        subprocess.check_output(['ping', '-c', '1', ip_address], stderr=subprocess.STDOUT, universal_newlines=True)
        print(f"Server {ip_address} is reachable.")
    except subprocess.CalledProcessError:
        print(f"Error: Server {ip_address} is not reachable.")

def main():
    # List of IP addresses
    server_ips = ['192.168.1.1', '8.8.8.8', '10.0.0.1']

    # Ping each server in the list
    for ip_address in server_ips:
        ping_server(ip_address)

if __name__ == "__main__":
    main()
