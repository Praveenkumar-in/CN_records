import socket

rec, port = 'localhost', 54321
b = 0

n = int(input("Enter number of frames to accept: "))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((rec, port))
    s.listen(1)

    print("Receiver is listening...")

    for i in range(n):
        b += 1
        connection, a = s.accept()

        with connection:
            print(f"Connection established with sender: {a}")
            d = connection.recv(1024).decode()
            print(f"Frame {b}: {d}")

            ack = "acknowledged"
            connection.sendall(ack.encode())
