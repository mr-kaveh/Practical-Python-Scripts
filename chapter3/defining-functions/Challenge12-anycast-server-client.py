## This code sets up a basic UDP server that listens for incoming messages,
## prints the received messages, and responds with a simple message.

# Server Code #
import socket

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Creates a new socket object using the IPv4 address family (AF_INET) and the UDP protocol (SOCK_DGRAM).
    server_socket.bind((host, port))
    # Binds the socket to the provided host and port, making it listen for incoming messages on that address.
    print(f"Server started at {host}:{port}")

    while True: # Listener Loop
        data, addr = server_socket.recvfrom(1024)
        # Receives data from any client that sends a message to the server. 
        # The recvfrom(1024) method reads up to 1024 bytes from the incoming message and returns the data and the address of the sender.
        print(f"Received message from {addr}: {data.decode()}")
        server_socket.sendto(b"Hello from server", addr)
        # Sends a response ("Hello from server") back to the client using the sender's address.

if __name__ == "__main__": # Checks if the script is being run directly (and not imported as a module).
    start_server('0.0.0.0', 96669)
    # server listens on all available network interfaces on Port 96669.




### ------------------ ###
## This code sets up a basic UDP client that sends a message to an Anycast IP address
## and waits for a reply from the "nearest server". It then prints the received reply.
# Client Code

import socket

def send_message(server_ip, port, message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Creates a new socket object using the IPv4 address family (AF_INET) and the UDP protocol (SOCK_DGRAM).
    client_socket.sendto(message.encode(), (server_ip, port))
    # Sends the encoded message to the specified server_ip and port. The sendto method sends the message as a UDP datagram.

    data, addr = client_socket.recvfrom(1024)
    print(f"Received reply from {addr}: {data.decode()}")
    # Waits for a reply from the server. The recvfrom(1024) method 
    # reads up to 1024 bytes from the incoming message and returns the data and the address of the sender.

if __name__ == "__main__": # Checks if the script is being run directly (and not imported as a module).
    anycast_ip = '203.0.113.0'  # Example Anycast IP
    send_message(anycast_ip, 96669, "Hello from client")

