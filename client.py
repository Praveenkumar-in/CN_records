import socket

def main():
    host = '127.0.0.1'
    port = 5555

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))
        print(f"Connected to server {host}:{port}")

        while True:
            message = input("You: ")
            client_socket.sendall(message.encode())

            data = client_socket.recv(1024)
            print("Server:", data.decode())

    except KeyboardInterrupt:
        print("\nClient shutting down...")

    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
