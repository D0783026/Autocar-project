import socket
import cv2
import numpy
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
ret, frame = capture.read()
encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]

print ("[*] Listening on %s:%d " % (TCP_IP,TCP_PORT))

flag1 = False
flag2 = False

while True:
    client, addr = s.accept()
    print ('Connected by ', addr)

    while True:

        #camera
        if ret:
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
        num1 = float(cut[2:5])
        num2 = float(cut[6:9])
        num3 = float(cut[10:13])
        num4 = float(cut[14:17])

        #控制車子移動
        flag1 = w.control_forward(num1)
        print('forward: ' + str(num1))
        flag2 = w.control_left(num2)
        print("left: " + str(num2))

        #車子靜止
        if flag1 == False and flag2 == False:
            w.stop()