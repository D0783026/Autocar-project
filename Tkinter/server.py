import socket
import cv2
import numpy

capture = cv2.VideoCapture(0)

TCP_IP = "0.0.0.0"
TCP_PORT = 9090
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(True)

ret, frame = capture.read()
encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]

print ("[*] Listening on %s:%d " % (TCP_IP,TCP_PORT))

while True:
    conn, addr = s.accept()
    print ('Connected by ', addr)
    while ret:
        result, imgencode = cv2.imencode('.jpg', frame, encode_param)
        data = numpy.array(imgencode)
        stringData = data.tostring()

        conn.send( str(len(stringData)).ljust(16).encode());
        conn.send( stringData );

        ret, frame = capture.read()
        decimg=cv2.imdecode(data,1)
        cv2.waitKey(30)

    conn.close()
    cv2.destroyAllWindows() 