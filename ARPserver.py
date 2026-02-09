import socket
from getmac import get_mac_address as gma

server_socket = socket.socket()
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Server started. Waiting for connections...")

while True:
    connection, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    with connection:
        data = gma()
        connection.send(data.encode())

 
