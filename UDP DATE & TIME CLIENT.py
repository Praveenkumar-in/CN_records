import socket

def main():
    server_address = ('localhost', 12345)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        message = "Request for Date and Time"
        sock.sendto(message.encode(), server_address)
        print("Received:", sock.recvfrom(4096)[0].decode())

if __name__ == "__main__":
    main()
