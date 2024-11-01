##  python code to use object oriented inheritence in monitoring network ports

# This module provides access to the BSD socket interface. 
# It is available on all modern Unix systems,
# Windows, MacOS, and probably additional platforms.
import socket

class PortMonitor:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def check_port(self):
        try:
            socket.create_connection((self.host, self.port), timeout=2)
            return True
        except (socket.timeout, ConnectionRefusedError):
            return False

class HTTPPortMonitor(PortMonitor):
    def __init__(self, host, port):
        super().__init__(host, port)

    def check_port(self):
        if super().check_port():
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((self.host, self.port))
                    s.sendall(b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n')
                    response = s.recv(1024)
                    if b'HTTP/1.1' in response:
                        return True
            except socket.timeout:
                return False
        return False

class UDPPortMonitor(PortMonitor):
    def __init__(self, host, port):
        super().__init__(host, port)

    def check_port(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.connect((self.host, self.port))
                return True
        except socket.timeout:
            return False

# Example usage
if __name__ == "__main__":
    host = 'example.com'
    http_port = 80
    udp_port = 12345

    http_monitor = HTTPPortMonitor(host, http_port)
    udp_monitor = UDPPortMonitor(host, udp_port)
    try:
      print(f"HTTP Port ({http_port}) status: {'Open' if http_monitor.check_port() else 'Closed'}")
      print(f"UDP Port ({udp_port}) status: {'Open' if udp_monitor.check_port() else 'Closed'}")
    except socket.error as err_msg:
      print(f"Socket ERROR! {err_msg}")
