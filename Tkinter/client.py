import socket
import cv2
import numpy

##receive all
def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

TCP_IP = "192.168.43.241"
TCP_PORT = 9090

sock = socket.socket()
sock.connect((TCP_IP, TCP_PORT))

##不斷接收資料
while 1:
    length = recvall(sock,16)
    stringData = recvall(sock, int(length))
    data = numpy.fromstring(stringData, dtype='uint8')
    decimg=cv2.imdecode(data,1)
    cv2.imshow('CLIENT2',decimg)
    cv2.waitKey(1)

sock.close()
cv2.destroyAllWindows()