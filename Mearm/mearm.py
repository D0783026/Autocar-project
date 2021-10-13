import RPi.GPIO as GPIO
import time
import curses
import sys

GPIO.setmode(GPIO.BCM) 
CONTROL_PIN_X = 5
CONTROL_PIN_Y = 6
CONTROL_PIN_Z = 22
CONTROL_PIN_S = 23  #夾子
PWM_FREQ = 50

angle_X=90
angle_Y=90
angle_Z=90
angle_S=0



GPIO.setup(CONTROL_PIN_X, GPIO.OUT)
GPIO.setup(CONTROL_PIN_Y, GPIO.OUT)
GPIO.setup(CONTROL_PIN_Z, GPIO.OUT)
GPIO.setup(CONTROL_PIN_S, GPIO.OUT)

pwm_X = GPIO.PWM(CONTROL_PIN_X, PWM_FREQ)
pwm_Y = GPIO.PWM(CONTROL_PIN_Y, PWM_FREQ)
pwm_Z = GPIO.PWM(CONTROL_PIN_Z, PWM_FREQ)
pwm_S = GPIO.PWM(CONTROL_PIN_S, PWM_FREQ)


def open_all():
   # global pwm_X, pwm_Y, pwm_Z, pwm_S
    print('ok')
    
    pwm_Y.start(100)
    pwm_X.start(100)
    pwm_Z.start(100)
    pwm_S.start(100)
    
    
    
def angle_to_duty_cycle(angle):
    duty_cycle = float(angle) /10 + 2.5
    return duty_cycle






def Base(x):
    global angle_X
    
    if x <= -0.5:
        dc = angle_to_duty_cycle(angle_X) 
        pwm_X.ChangeDutyCycle(dc)
        dc=0
        
        if angle_X>=180:
            pass
        else:
            angle_X+=3
        return True
        
    elif x >= 0.5:
        dc = angle_to_duty_cycle(angle_X) 
        pwm_X.ChangeDutyCycle(dc)
        dc=0
        
        if angle_X<=0:
            pass
        else:
            angle_X-=3
        return True
    
    else:
        return False
    
    
    
def control_Forward_Backward(x):
    global angle_Y
    if x <= -0.5: 
        dc = angle_to_duty_cycle(angle_Y) 
        pwm_Y.ChangeDutyCycle(dc)
        dc=0
        if angle_Y>=180:
            pass
        else:
            angle_Y+=3
        return True
    
    elif x >= 0.5:
        
        dc = angle_to_duty_cycle(angle_Y) 
        pwm_Y.ChangeDutyCycle(dc)
        dc=0
        if angle_Y<=0:
            pass
        else:
            angle_Y-=3
        return True
    else:
        return False
    
    
    

def control_High_Low(but_Y,but_A):
    global angle_Z
    if but_Y == 1 and but_A == 0: 
        dc = angle_to_duty_cycle(angle_Z) 
        pwm_Z.ChangeDutyCycle(dc)
        dc=0
        if angle_Z>=180:
            pass
        else:
            angle_Z+=3
        return True
    
    elif but_A == 1 and but_Y == 0:
        dc = angle_to_duty_cycle(angle_Z) 
        pwm_Z.ChangeDutyCycle(dc)     
        dc=0
        if angle_Z<=0:
            pass
        else:
            angle_Z-=3
        return True
    else:
        return False
    
    

def control_Scissor(but_X,but_B):
    global angle_S
    if but_X == 1 : 
        angle_S=180
        dc = angle_to_duty_cycle(angle_S) 
        pwm_S.ChangeDutyCycle(dc)
        dc=0
        return True
    
    elif but_B == 1:
        angle_S=0
        dc = angle_to_duty_cycle(angle_S) 
        pwm_S.ChangeDutyCycle(dc)       
        dc=0
        return True
    else:
        return False
    
    
    
    

