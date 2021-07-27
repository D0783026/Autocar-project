import tkinter as tk #大小寫要注意,如果小寫不行就改大寫
import time
from PIL import  ImageTk, Image, ImageDraw
import cv2
import random

captrue = cv2.VideoCapture(0) #開啟相機，0為預設筆電內建相機
captrue.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')) #設置影像參數
captrue.set(3,350) #像素
captrue.set(4,500) #像素


img_viode = 'D:\\a.jpg'    #影像存放位置 要改


def check():
    global captrue
    if captrue.isOpened(): #判斷相機是否有開啟
        open()
    else:
        captrue = cv2.VideoCapture(0) 
        captrue.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')) #設置影像參數
        captrue.set(3,350) #像素
        captrue.set(4,500) #像素
        open()
        


def open():
    global s
    ret,frame = captrue.read() #取得相機畫面
    cv2.imwrite(img_viode,frame) #儲存圖片
    img_right = ImageTk.PhotoImage(Image.open(img_viode)) #讀取圖片
    label_right.imgtk=img_right #換圖片
    label_right.config(image=img_right) #換圖片
    s = label_right.after(1, open) #持續執行open方法，1000為1秒

def close():
    captrue.release() #關閉相機
    label_right.after_cancel(s) #結束拍照
    label_right.config(image=img) #換圖片

#創建一個視窗
top = tk.Tk() 
#視窗名稱
top.title('GUI') 
#寬:300高:200的視窗,放在寬:600高:300的位置
top.geometry('600x500+200+100') 

#開啟照片
img= ImageTk.PhotoImage(Image.open('D:\\畢業專題\\Tkinter\\a.jpg')) #要改

#用label來放照片
label_right= tk.Label(top,height=360,width=480,bg ='gray94',fg='blue',image = img) 

#按鈕
button_1 = tk.Button(top,text = 'open',bd=4,height=4,width=22,bg ='gray94',command =check)
button_2 = tk.Button(top,text = 'close',bd=4,height=4,width=22,bg ='gray94',command =close)

#位置
label_right.grid(row=1,column=0,padx=20, pady=20, sticky="nw") 
button_1.grid(row=1, column=0, padx=100, pady=400, sticky="nw")  
button_2.grid(row=1, column=0, padx=300, pady=400, sticky="nw") 
top.mainloop() #執行視窗