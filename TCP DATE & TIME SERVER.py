import socket
from datetime import datetime

# Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind host and port
s.bind(("127.0.0.1", 1025))

# Listen for connections
s.listen(5)
print("TCP Date & Time Server is running...")

while True:
    clt, adr = s.accept()
    print(f"aConnection to {adr} established")

    # Get current date and time
    now = datetime.now()
    message = now.strftime("Date: %Y-%m-%d | Time: %H:%M:%S")

    # Send to client
    clt.send(message.encode("utf-8"))
    clt.close()
