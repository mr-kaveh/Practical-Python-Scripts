#  prints unique IPs nginx Access logs file
import re

nginx_log_file_path = '/var/log/nginx/access.log'

def extract_client_ips(log_file_path):
    client_ips = set()

    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            # Use a regular expression to extract the client IP address from the log entry
            # d+\. means 1 or more digits followed by a .(dot)
            match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
            if match:
                client_ip = match.group(1)
                client_ips.add(client_ip)

    return client_ips

##
# calling the function and creating a list of client_ips
client_ips = extract_client_ips(nginx_log_file_path)

print("Unique client IP addresses:")
for ip in client_ips:
    print(ip)
