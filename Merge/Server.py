import socket
import cv2
import numpy
from enum import Enum
import controlWheel as w


#open camera
capture = cv2.VideoCapture(0)

#set socket
TCP_IP = "0.0.0.0"
TCP_PORT = 9090
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(True)

#camera read
frame = capture.read()
encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]

print ("[*] Listening on %s:%d " % (TCP_IP,TCP_PORT))

class State(Enum):
    Forward = 1
    Left = 2

state = 1

while True:
    client, addr = s.accept()
    print ('Connected by ', addr)

    while True:

        #camera
        result, imgencode = cv2.imencode('.jpg', frame, encode_param)
        data = numpy.array(imgencode)
        stringData = data.tostring()

        client.send( str(len(stringData)).ljust(16).encode());
        client.send( stringData );

        frame = capture.read()
        decimg=cv2.imdecode(data,1)
        cv2.waitKey(30)

        #wheel and mearm
        value = client.recv(1024)

        if state == State.Forward:
            flag1 = w.control_forward(value)
            state += 1
        elif state == State.Left:
            flag2 = w.control_left(value)
            state = 1
        
        if flag1 == False and flag2 == False:
            w.stop()



client.close()
cv2.destroyAllWindows()