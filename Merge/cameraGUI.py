from os import times
import tkinter as tk
from tkinter.constants import NW #大小寫要注意,如果小寫不行就改大寫
from PIL import  ImageTk, Image, ImageDraw
import cv2
import socket
import numpy
from numpy.lib.arraypad import pad
import pygame
import threading
import time

pygame.init()

# Initialize the joysticks
pygame.joystick.init()

joystick_count = pygame.joystick.get_count()

for i in range(joystick_count):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()


##receive all
def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

TCP_IP = "172.20.10.4"
TCP_PORT = 9000

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


def sendText():
    global label_2, label_4
    while True:

        # SENDING DATA
        cmd2 = str(joystick.get_axis(1)) #control forward and backward
        cmd2 = cmd2[0:4]
        print('cmd2 : ' + cmd2)
        if cmd2 == '0.0':
            cmd2 = cmd2 + '0'

        cmd1 = str(joystick.get_axis(0)) #control left and right
        cmd1 = cmd1[0:4]
        if cmd1 == '0.0':
            cmd1 = cmd1 + '0'

        cmd3 = str(joystick.get_axis(2))
        cmd3 = cmd3[0:4]
        if cmd3 == '0.0':
                cmd3 = cmd3 + '0'

        cmd4 = str(joystick.get_axis(3))
        cmd4 = cmd4[0:4]
        if cmd4 == '0.0':
                cmd4 = cmd4 + '0'

        
        but_Y = str(joystick.get_button(3))
        but_A = str(joystick.get_button(0))
        but_X = str(joystick.get_button(2))
        but_B = str(joystick.get_button(1))

        cmd = cmd1 + cmd2 + cmd3 + cmd4 + but_Y + but_A + but_X + but_B
        print(cmd1 + '|' + cmd2 + '|' + cmd3 + '|' + cmd4  + '|' + but_Y + '|' + but_A)
        print('cmd : ' + cmd)
        
        #要按open controller才能操作
        '''if label_2['text'] == 'Closed':
            cmd = '0.000.000.000.000000'
        else:
            if joystick.get_axis(1) <= -0.5:
                label_4['text'] = 'Forward'
            elif joystick.get_axis(1) >= 0.5:
                label_4['text'] = 'Backward'
            elif joystick.get_axis(0) <= -0.5:
                label_4['text'] = 'turn Left'
            elif joystick.get_axis(0) >= 0.5:
                label_4['text'] = 'turn Right'
            else:
                label_4['text'] = 'Stopped'''

        sock.send(cmd.encode())
        time.sleep(0.05)

def openStick():
    global label_2
    label_2['text'] = 'Opened'

def closeStick():
    global label_2,label_4
    label_2['text'] = 'Closed'

#創建一個視窗
top = tk.Tk()
#視窗名稱
top.title('拆彈機器人')
#設定視窗大小
top.geometry('800x500') #寬*高
align_mode = 'nswe'
pad = 5

#開啟照片
img= ImageTk.PhotoImage(Image.open('D:\\畢業專題\\Tkinter\\000.jpg'))

div1 = tk.Frame(top,height=400, width = 480, bg = 'orange')
div2 = tk.Frame(top,height=60, width=480)
div3 = tk.Frame(top,height=460, width= 35, bg = 'green')

div1.grid(column=0,row=0, padx=pad,pady=pad, sticky=align_mode)
div2.grid(column=0, row=1,columnspan=2, padx=pad, pady=pad, sticky=align_mode)
div3.grid(column=1, row=0,rowspan=2, padx=pad,pady=pad,sticky=align_mode)

#用label來放照片
label_right= tk.Label(div1,height = 360,width=480, bg ='gray94',fg='blue',image = img) 

#按鈕
button_1 = tk.Button(div2,text = 'open Controller',bd=4,height=4,width=15,bg ='gray94',command =openStick)
button_2 = tk.Button(div2,text = 'close Controller',bd=4,height=4,width=15,bg ='gray94',command =closeStick)

#小車狀態
label_1 = tk.Label(div3, text = 'Controller : ',font=(16),width=20, bg='yellow',anchor='w')
label_2 = tk.Label(div3,text = 'Closed',font=('Arial', 16),width=20, bg='yellow')
label_3 = tk.Label(div3, text = 'Car State : ',font=(16),width=20, bg='yellow',anchor='w')
label_4 = tk.Label(div3,text = 'Stopped',font=('Arial', 16),width=20, bg='yellow')

#位置
label_right.grid(row=0, column=0, padx=20, pady=20, sticky="nw")

button_1.grid(row=0, column=0,padx=40, sticky=align_mode)
button_2.grid(row=0, column=1, sticky=align_mode)

label_1.grid(row=0,column=0,sticky=align_mode)
label_2.grid(row=1, column=0,pady=pad, sticky=align_mode)
label_3.grid(row=2,column=0,sticky=align_mode)
label_4.grid(row=3, column=0,pady=pad, sticky=align_mode)

#加開兩個threading來做 socket 的 send 跟 recv
t1 = threading.Thread(target=open)
t = threading.Thread(target=sendText)
t1.start()
t.start()
top.mainloop() #執行視窗