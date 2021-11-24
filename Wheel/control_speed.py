#!/usr/bin/python
# -*- coding: utf-8-*-

from enum import Enum
import RPi.GPIO as GPIO
import socket

#set socket
bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)

print ("[*] Listening on %s:%d " % (bind_ip,bind_port))

#setting GPIO
GPIO.setmode(GPIO.BCM)

RIN1 = 13       #白
RIN2 = 16       #橘
RIN3 = 19       #灰
RIN4 = 20       #紫
LIN1 = 15        #紅
LIN2 = 4       #藍
LIN3 = 17       #黃
LIN4 = 18       #綠

ENR_A = 12
ENR_B = 21
ENL_A = 14
ENL_B = 27

GPIO.setup(RIN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RIN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RIN3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RIN4, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LIN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LIN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LIN3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LIN4, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(ENR_A, GPIO.OUT)
GPIO.setup(ENR_B, GPIO.OUT)
GPIO.setup(ENL_A, GPIO.OUT)
GPIO.setup(ENL_B, GPIO.OUT)

pwm_R_A = GPIO.PWM(ENR_A,500)  #ENR_A设置为PWM控制
pwm_R_B = GPIO.PWM(ENR_B,500)  #ENR_B设置为PWM控制
pwm_L_A = GPIO.PWM(ENL_A,500)  #ENL_A设置为PWM控制
pwm_L_B = GPIO.PWM(ENL_B,500)  #NL_B设置为PWM控制

pwm_R_A.start(50)
pwm_R_B.start(50)
pwm_L_A.start(50)
pwm_L_B.start(50)

class State(Enum):
    Forward = 1
    Left = 2

state = 1


while True:
    client,addr = server.accept()
    print ('Connected by ', addr)
    
    while True:
        data = client.recv(1024)
        print ("Client recv data : %s " % (data))

        state += 1

        if state == State.Forward:
            float1 = float(data)
        elif state == State.Left:
            float2 = float(data)
            state = 1
        
        if float1 >= 0.8 and float1 <= 1.2 and float2 >= 2.8 and float2 <= 3.2:
            GPIO.output(LIN1, GPIO.LOW)     #GPIO17
            GPIO.output(LIN2, GPIO.LOW)     #GPIO18
            GPIO.output(LIN3, GPIO.LOW)     #GPIO22
            GPIO.output(LIN4, GPIO.LOW)     #GPIO23
            GPIO.output(RIN1, GPIO.LOW)     #GPIO7
            GPIO.output(RIN2, GPIO.LOW)     #GPIO11
            GPIO.output(RIN3, GPIO.LOW)     #GPIO25
            GPIO.output(RIN4, GPIO.LOW)     #GPIO10
            #GPIO.cleanup()       #清除GPIO資料

        # Forward
        if float(data) >= 2.0 and float(data) <= 2.5:
            
            GPIO.output(LIN1, GPIO.LOW)
            GPIO.output(LIN2, GPIO.HIGH)
            GPIO.output(LIN3, GPIO.LOW)
            GPIO.output(LIN4, GPIO.HIGH)
            GPIO.output(RIN1, GPIO.LOW)
            GPIO.output(RIN2, GPIO.HIGH)
            GPIO.output(RIN3, GPIO.LOW)
            GPIO.output(RIN4, GPIO.HIGH)
        

        # Backward
        elif float(data) >= 3.5:
            
            GPIO.output(LIN1, GPIO.HIGH)
            GPIO.output(LIN2, GPIO.LOW)
            GPIO.output(LIN3, GPIO.HIGH)
            GPIO.output(LIN4, GPIO.LOW)
            GPIO.output(RIN1, GPIO.HIGH)
            GPIO.output(RIN2, GPIO.LOW)
            GPIO.output(RIN3, GPIO.HIGH)
            GPIO.output(RIN4, GPIO.LOW)

        # Turn Right
        elif float(data) >= 0.5 and float(data) <= 1.0:
            
            GPIO.output(LIN1, GPIO.LOW)
            GPIO.output(LIN2, GPIO.HIGH)
            GPIO.output(LIN3, GPIO.LOW)
            GPIO.output(LIN4, GPIO.HIGH)
            GPIO.output(RIN1, GPIO.LOW)
            GPIO.output(RIN2, GPIO.LOW)
            GPIO.output(RIN3, GPIO.LOW)
            GPIO.output(RIN4, GPIO.LOW)

        # Turn Left
        elif float(data) <= -0.5:
            
            GPIO.output(LIN1, GPIO.LOW)
            GPIO.output(LIN2, GPIO.LOW)
            GPIO.output(LIN3, GPIO.LOW)
            GPIO.output(LIN4, GPIO.LOW)
            GPIO.output(RIN1, GPIO.LOW)
            GPIO.output(RIN2, GPIO.HIGH)
            GPIO.output(RIN3, GPIO.LOW)
            GPIO.output(RIN4, GPIO.HIGH)