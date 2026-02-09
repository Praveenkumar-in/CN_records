import socket

def echo_server(host, port):
    try:
        with socket.create_server((host, port)) as server_socket:
            print(f"Echo server is listening on {host}:{port}")

            while True:
                client_socket, client_address = server_socket.accept()
                print("Connected from", client_address)

                with client_socket:
                    while True:
                        data = client_socket.recv(1024)
                        if not data:
                            break
                        client_socket.sendall(data)
                        print(f"Received and echoed: {data.decode()}")

    except KeyboardInterrupt:
        print("\nServer stopped")

if __name__ == "__main__":
    echo_server("127.0.0.1", 12345)
