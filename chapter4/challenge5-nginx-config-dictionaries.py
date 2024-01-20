#  use dictioneries to keep nginx configurations
#
# Function to generate Nginx configuration from a dictionary
def generate_nginx_config(config_dict):
    config_lines = []
    
    for key, value in config_dict.items():
        config_lines.append(f"{key} {value};")

    return "\n".join(config_lines)

# Sample Nginx configuration dictionary
nginx_config = {
    'server_name': 'example.com',
    'listen': '80',
    'root': '/var/www/html',
    'index': 'index.html',
    'location /images/': {
        'alias': '/var/www/images/',
    },
    'error_page': '404 /404.html',
}

# Generate and print the Nginx configuration
nginx_config_str = generate_nginx_config(nginx_config)
print(nginx_config_str)
