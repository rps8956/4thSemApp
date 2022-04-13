import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1025))
s.listen(5)
while True:
    clt,adr = s.accept()
    print(f"Conection to {adr} established")
    clt.send(bytes("Socket programing in python","utf-8"))
    clt.close()
