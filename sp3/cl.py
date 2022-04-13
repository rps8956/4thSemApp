import socket
PORT = 9999

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((socket.gethostname(),PORT))
print(c.recv(1024).decode())
name = input("Enter your name")
c.send(bytes(name,"utf-8"))
