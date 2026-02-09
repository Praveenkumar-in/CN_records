import socket

def echo_client():
    with socket.create_connection(("127.0.0.1", 12345)) as client_socket:
        while True:
            message = input("Enter message to send (type 'exit' to quit): ")
            if message == "exit":
                break

            client_socket.sendall(message.encode())
            reply = client_socket.recv(1024).decode()
            print("Server:", reply)

if __name__ == "__main__":
    echo_client()
