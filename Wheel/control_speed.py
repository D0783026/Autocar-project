import RPi.GPIO as GPIO
import curses
import time
from curses import wrapper

GPIO.setmode(GPIO.BCM)

RIN1 = 8        #白
RIN2 = 25       #橘
RIN3 = 24       #灰
RIN4 = 23       #紫
LIN1 = 4        #紅
LIN2 = 14       #藍
LIN3 = 15       #黃
LIN4 = 18       #綠

ENR_A = 6
ENR_B = 12
ENL_A = 2
ENL_B = 3

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

stdscr = curses.initscr()
stdscr.clear()
pwm_R_A = GPIO.PWM(ENR_A,500)  #ENR_A设置为PWM控制
pwm_R_B = GPIO.PWM(ENR_B,500)  #ENR_B设置为PWM控制
pwm_L_A = GPIO.PWM(ENL_A,500)  #ENL_A设置为PWM控制
pwm_L_B = GPIO.PWM(ENL_B,500)  #NL_B设置为PWM控制

pwm_R_A.start(0)
pwm_R_B.start(0)
pwm_L_A.start(0)
pwm_L_B.start(0)


def Speed_Control(x):
    value=0
    global pwm_L_A, pwm_L_B, pwm_R_A, pwm_R_B
    if x == 'q':
        pwm_R_A.ChangeDutyCycle(0)
        pwm_L_A.ChangeDutyCycle(0)
        pwm_R_B.ChangeDutyCycle(0)
        pwm_L_B.ChangeDutyCycle(0)
        

    elif x == 'w':
        pwm_R_A.ChangeDutyCycle(100)
        pwm_L_A.ChangeDutyCycle(100)
        pwm_R_B.ChangeDutyCycle(100)
        pwm_L_B.ChangeDutyCycle(100)
        
    elif x == 'x':
        pwm_R_A.ChangeDutyCycle(100)
        pwm_L_A.ChangeDutyCycle(100)
        pwm_R_B.ChangeDutyCycle(100)
        pwm_L_B.ChangeDutyCycle(100)
    
    elif x == 'a':
        pwm_R_A.ChangeDutyCycle(100)
        pwm_R_B.ChangeDutyCycle(100)
        

    elif x == 'd':
        
        pwm_L_A.ChangeDutyCycle(100)
        pwm_L_B.ChangeDutyCycle(100)


while True:
    ch = stdscr.getkey()
# Quit
    if ch == 'q':
       curses.endwin()
       Speed_Control(ch)
       
       GPIO.output(LIN1, GPIO.LOW)     #GPIO17
       GPIO.output(LIN2, GPIO.LOW)     #GPIO18
       GPIO.output(LIN3, GPIO.LOW)     #GPIO22
       GPIO.output(LIN4, GPIO.LOW)     #GPIO23
       GPIO.output(RIN1, GPIO.LOW)     #GPIO7
       GPIO.output(RIN2, GPIO.LOW)     #GPIO11
       GPIO.output(RIN3, GPIO.LOW)     #GPIO25
       GPIO.output(RIN4, GPIO.LOW)     #GPIO10
       
       GPIO.cleanup()       #清除GPIO資料
      

       break

# Forward
    elif ch == 'w':
       Speed_Control(ch)
       GPIO.output(LIN1, GPIO.LOW)
       GPIO.output(LIN2, GPIO.HIGH)
       GPIO.output(LIN3, GPIO.LOW)
       GPIO.output(LIN4, GPIO.HIGH)
       GPIO.output(RIN1, GPIO.HIGH)
       GPIO.output(RIN2, GPIO.LOW)
       GPIO.output(RIN3, GPIO.LOW)
       GPIO.output(RIN4, GPIO.HIGH)
       

# Backward
    elif ch == 'x':
       Speed_Control(ch)
       GPIO.output(LIN1, GPIO.HIGH)
       GPIO.output(LIN2, GPIO.LOW)
       GPIO.output(LIN3, GPIO.HIGH)
       GPIO.output(LIN4, GPIO.LOW)
       GPIO.output(RIN1, GPIO.LOW)
       GPIO.output(RIN2, GPIO.HIGH)
       GPIO.output(RIN3, GPIO.HIGH)
       GPIO.output(RIN4, GPIO.LOW)

# Turn Right
    elif ch == 'd':
       Speed_Control(ch)
       GPIO.output(LIN1, GPIO.LOW)
       GPIO.output(LIN2, GPIO.HIGH)
       GPIO.output(LIN3, GPIO.LOW)
       GPIO.output(LIN4, GPIO.HIGH)
       GPIO.output(RIN1, GPIO.LOW)
       GPIO.output(RIN2, GPIO.LOW)
       GPIO.output(RIN3, GPIO.LOW)
       GPIO.output(RIN4, GPIO.LOW)

# Turn Left
    elif ch == 'a':
       Speed_Control(ch)
       GPIO.output(LIN1, GPIO.LOW)
       GPIO.output(LIN2, GPIO.LOW)
       GPIO.output(LIN3, GPIO.LOW)
       GPIO.output(LIN4, GPIO.LOW)
       GPIO.output(RIN1, GPIO.HIGH)
       GPIO.output(RIN2, GPIO.LOW)
       GPIO.output(RIN3, GPIO.LOW)
       GPIO.output(RIN4, GPIO.HIGH)


GPIO.cleanup()       #清除GPIO資料