import socket

# Connect to server
with socket.create_connection(("127.0.0.1", 1025)) as s:
    message = s.recv(1024).decode("utf-8")
    print("Server Response:")
    print(message)
