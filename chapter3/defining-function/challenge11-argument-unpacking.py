# System administration often involves dealing with various configurations and parameters. 
# Here's an advanced Python script that utilizes argument unpacking to perform common system administration tasks,
# such as managing users and services. This script demonstrates how to use argument unpacking to make the code more flexible and adaptable.

import subprocess

# Function to add a new user with optional arguments
def add_user(username, password=None, shell='/bin/bash'):
    cmd = ['useradd', username, '-s', shell]
    
    if password:
        cmd.extend(['-p', password])
    
    subprocess.run(cmd)
    print(f"User {username} created")

# Function to start or stop a service
def manage_service(service_name, action='start'):
    cmd = ['systemctl', action, service_name]
    subprocess.run(cmd)
    print(f"Service {service_name} {action}ed")

# Unpacking arguments to add a user and manage services
user_info = {'username': 'john_doe', 'password': 'my_password'}
add_user(**user_info)

service_info = {'service_name': 'apache2', 'action': 'stop'}
manage_service(**service_info)
