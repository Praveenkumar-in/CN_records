import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)

try:
    client_socket.connect(server_address)

    MAC = input("Enter MAC Address (format: XX:XX:XX:XX:XX:XX): ")
    client_socket.send(MAC.encode())

    received_data = client_socket.recv(1024)
    ip_address = received_data.decode()

    print(f"IP Address: {ip_address}")

finally:
    client_socket.close()