import socket

HOST = '192.168.43.105'
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST , PORT))

while True:
    cmd = input("Please input msg:")
    s.send(cmd.encode())
    s.send("okok".encode())
    data = s.recv(1024).decode()
    print ("server send : %s " % (data))