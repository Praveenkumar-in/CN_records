import socket

def main():
    host = '127.0.0.1'
    port = 5555

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}")

    client_socket, address = server_socket.accept()
    print("Connection from:", address)

    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break

            print("Received from client:", data.decode())
            client_socket.sendall(data)  # Echo back

    except KeyboardInterrupt:
        print("\nServer shutting down...")

    finally:
        client_socket.close()
        server_socket.close()

if __name__ == "__main__":
    main()
