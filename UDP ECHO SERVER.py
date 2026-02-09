import socket

def echo_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"Echo server is listening on {host}:{port}")

        while True:
            data, addr = s.recvfrom(1024)
            print(f"Received from {addr}: {data.decode()}")
            s.sendto(data, addr)
            print(f"Echoed back to {addr}")

if __name__ == "__main__":
    echo_server("127.0.0.1", 12345)
