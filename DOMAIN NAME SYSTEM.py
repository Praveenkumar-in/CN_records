import socket

url = str(input("Enter URL: "))
addr = socket.gethostbyname(url)
print(addr)
