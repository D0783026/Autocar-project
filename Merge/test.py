from multiprocessing import Process
import os
import tkinter as tk #大小寫要注意,如果小寫不行就改大寫
from PIL import  ImageTk, Image, ImageDraw
import cv2
import socket
import numpy
from numpy.lib.arraypad import pad
import pygame
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


img_viode = 'D:\\a.jpg' #圖片存放位置


def open():
    '''global s
    length = recvall(sock,16)
    stringData = recvall(sock, int(length))
    data = numpy.fromstring(stringData, dtype='uint8')
    decimg=cv2.imdecode(data,1)
    cv2.waitKey(1)
    cv2.imwrite(img_viode,decimg) #儲存圖片
    img_right = ImageTk.PhotoImage(Image.open(img_viode)) #讀取圖片
    label_right.imgtk=img_right #換圖片
    label_right.config(image=img_right) #換圖片
    s = label_right.after(1, open) #持續執行open方法，1000為1秒'''

def close():
    cv2.destroyAllWindows()
    #label_right.after_cancel(s) #結束拍照
    label_right.config(image=img) #換圖片


#記錄小車狀態
carState = 'nothing'

def control():
    global c
    if joystick.get_axis(1) <= -0.5:
        carState = 'Forward'
        print("upupupup!!!")
    if joystick.get_axis(1) >= 0.5:
        carState = 'Backward'
        print("downdown!!!")
    if joystick.get_axis(0) <= -0.5:
        carState = 'Left'
        print("leftleft!!!")
    if joystick.get_axis(0) >= 0.5:
        carState = 'Right'
        print("rightright!")

    '''cmd2 = str(joystick.get_axis(1))
    sock.send(cmd2.encode()) #control forward and backward

    cmd1 = str(joystick.get_axis(0))
    sock.send(cmd1.encode()) #control left and right'''
    c = carState.after(1, control)

#創建一個視窗
top = tk.Tk()
#視窗名稱
top.title('拆彈機器人')
#設定視窗大小
top.geometry('800x500') #寬*高

#開啟照片
img= ImageTk.PhotoImage(Image.open('D:\\畢業專題\\Tkinter\\000.jpg'))

#用label來放照片
label_right= tk.Label(top,height=360,width=480,bg ='gray94',fg='blue',image = img) 

#按鈕
button_1 = tk.Button(top,text = 'open Camera',bd=4,height=4,width=15,bg ='gray94',command =open)
button_2 = tk.Button(top,text = 'close Camera',bd=4,height=4,width=15,bg ='gray94',command =close)
button_3 = tk.Button(top,text = 'open Controller',bd=4,height=4,width=15,bg ='gray94',command =control)

#小車狀態
label_1 = tk.Label(top,text = carState,height=10,width=35,bg='yellow',fg='blue')

#位置
label_right.grid(row=0, column=0, columnspan=3, padx=20, pady=20, sticky="nw")

button_1.grid(row=1, column=0, padx = 30, pady=5, sticky="nw")
button_2.grid(row=1, column=1, pady=5, sticky="nw")
button_3.grid(row=1, column=2, pady=5, sticky="nw")

label_1.grid(row=0, column=3, pady = 20, sticky="nw")

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)
    top.mainloop()

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()