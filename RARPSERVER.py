import socket
import ipaddress

def convert_mac_to_ip(mac_address):
    try:
        mac_bytes = [int(x, 16) for x in mac_address.split(":")]

        if len(mac_bytes) != 6:
            return "Invalid MAC format"

        # Simple MAC → pseudo IP conversion
        mac_bytes[0] ^= 0x02
        ip_address = ipaddress.IPv4Address(
            f"169.254.{mac_bytes[4]}.{mac_bytes[5]}"
        )

        return str(ip_address)

    except Exception:
        return "Error processing MAC"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Server started. Waiting for connections...")

while True:
    connection, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    MAC = connection.recv(1024).decode()
    ip_address = convert_mac_to_ip(MAC)

    connection.send(ip_address.encode())
    print("IP address returned to client")

    connection.close()