import socket

sender_host, sender_port = 'localhost', 12345
receiver_host, receiver_port = 'localhost', 54321

n = int(input("Enter number of frames: "))

for i in range(n):
    message = input(f"Enter message for frame {i+1}: ")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sender_socket:
        sender_socket.connect((receiver_host, receiver_port))
        sender_socket.send(message.encode())

        data = sender_socket.recv(1024)
        print("Received from receiver:", data.decode())
