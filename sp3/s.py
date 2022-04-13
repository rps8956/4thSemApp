import socket
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),PORT))
s.listen(5)
print("Connecting...........")

while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send(bytes("Welcooooooome", "utf-8"))
    name = c.recv(1024).decode()
    print(name)

    c.close()