import socket
from datetime import datetime

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind(("localhost", 12345))
        print("UDP Date and Time Server is running...")

        while True:
            data, addr = s.recvfrom(4096)
            print("Received:", data.decode(), "from", addr)
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            s.sendto(current_time.encode(), addr)

if __name__ == "__main__":
    main()
