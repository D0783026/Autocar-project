import socket
import cv2
import numpy
from enum import Enum
import controlWheel as w
import MeArm as m
import time

m.open_all()
#open camera
capture = cv2.VideoCapture(0)

#set socket
TCP_IP = "0.0.0.0"
TCP_PORT = 9000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(True)

#camera read
ret, frame = capture.read()
encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]

print ("[*] Listening on %s:%d " % (TCP_IP,TCP_PORT))



state = 1
flag1 = False
flag2 = False
flag3 = False
flag4 = False
flag5 = False
flag6 = False
while True:
    client, addr = s.accept()
    print ('Connected by ', addr)
     
    while True:
        
        
        if ret:

            #camera
            result, imgencode = cv2.imencode('.jpg', frame, encode_param)
            data = numpy.array(imgencode)
            stringData = data.tostring()

            client.send( str(len(stringData)).ljust(16).encode());
            client.send( stringData );

            ret, frame = capture.read()
            decimg=cv2.imdecode(data,1)
            cv2.waitKey(30)
        
        #wheel and mearm
        value = client.recv(1024)
        cut = str(value)
        print(cut)
        
        num1 = float(cut[2:5])
        num2 = float(cut[6:9])
        num3 = float(cut[10:13])
        num4 = float(cut[14:17])
        but_Y = int(cut[18])
        but_A = int(cut[19])
        but_X = int(cut[20])
        but_B = int(cut[21])
        print(str(num1)+' '+str(num2)+' '+str(num3)+' '+str(num4)+' '+str(but_Y)+' '+str(but_A)+' ' + str(but_X)+' ' + str(but_B))
        
        
        flag1 = w.control_forward(num2)
        print('forward: ' + str(flag1))
        
        flag2 = w.control_left(num1)
        print("left: " + str(flag2))
        

        flag3 = m.Base(num3)
        print("Mearm_Base: " + str(flag3))

        flag4 = m.control_Forward_Backward(num4)
        print("Mearm_Forward: " + str(flag4))
        
        flag5 = m.control_High_Low(but_Y,but_A)
        print("Mearm_high: " + str(flag5))
            
        flag6 = m.control_Scissor(but_X,but_B)
        print("Mearm_Scissor: " + str(flag6))
        
        if flag1 == False and flag2 == False:
            w.stop()
        

client.close()
cv2.destroyAllWindows()