import socket

def echo_client():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        server_address = ('localhost', 12345)

        while True:
            message = input("Enter message (type 'exit' to quit): ")
            if message == "exit":
                break

            client_socket.sendto(message.encode(), server_address)
            data, _ = client_socket.recvfrom(1024)
            print("Server:", data.decode())

if __name__ == "__main__":
    echo_client()
