import socket

client_socket = socket.create_connection(('localhost', 12345))

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

try:
    print("Host IP:", IPAddr)
    received_data = client_socket.recv(1024)
    print(f"Mac address: {received_data.decode()}")
finally:
    client_socket.close()

