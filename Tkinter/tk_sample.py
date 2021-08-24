import tkinter as tk #大小寫要注意,如果小寫不行就改大寫
import time
from PIL import  ImageTk, Image, ImageDraw
import cv2
import random
import socket
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
TCP_PORT = 9091

sock = socket.socket()
sock.connect((TCP_IP, TCP_PORT))


img_viode = 'D:\\a.jpg' #圖片存放位置
        


def open():
    global s
    length = recvall(sock,16)
    stringData = recvall(sock, int(length))
    data = numpy.fromstring(stringData, dtype='uint8')
    decimg=cv2.imdecode(data,1)
    cv2.waitKey(1)
    cv2.imwrite(img_viode,decimg) #儲存圖片
    img_right = ImageTk.PhotoImage(Image.open(img_viode)) #讀取圖片
    label_right.imgtk=img_right #換圖片
    label_right.config(image=img_right) #換圖片
    s = label_right.after(1, open) #持續執行open方法，1000為1秒

def close():
    cv2.destroyAllWindows()
    label_right.after_cancel(s) #結束拍照
    label_right.config(image=img) #換圖片

def send():
    sock.send("TEST!".encode())


#創建一個視窗
top = tk.Tk() 
#視窗名稱
top.title('拆彈機器人')
#設定視窗大小
top.geometry('550x500')

#開啟照片
img= ImageTk.PhotoImage(Image.open('D:\\畢業專題\\Tkinter\\000.jpg'))

#用label來放照片
label_right= tk.Label(top,height=360,width=480,bg ='gray94',fg='blue',image = img) 

#按鈕
button_1 = tk.Button(top,text = 'open',bd=4,height=4,width=22,bg ='gray94',command =open)
button_2 = tk.Button(top,text = 'close',bd=4,height=4,width=22,bg ='gray94',command =close)

#位置
label_right.grid(row=1,column=0,padx=20, pady=20, sticky="nw") 
button_1.grid(row=1, column=0, padx=100, pady=400, sticky="nw")  
button_2.grid(row=1, column=0, padx=300, pady=400, sticky="nw")
top.mainloop() #執行視窗