import socket

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('', 8888)  # Listen on all available network interfaces
server_socket.bind(server_address)

# Start listening for incoming connections
server_socket.listen(1)  # The argument specifies the maximum number of queued connections

print(f"Listening on port 8888...")

while True:
    # Wait for a client to connect
    client_socket, client_address = server_socket.accept()
    
    print(f"Connection from {client_address}")
    
    # Handle the connection (you can add your own logic here)
    client_socket.send(b"Welcome to the server!")
    
    # Close the client socket
    client_socket.close()
