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

angle_X=108.0
angle_Y=18.0
angle_Z=72.0
angle_S=140.0



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
    angle_X=108.0
    angle_Y=18.0
    angle_Z=72.0
    angle_S=140.0
    pwm_Y.start(0)
    pwm_X.start(0)
    pwm_Z.start(0)
    pwm_S.start(0)
    
    pwm_Y.ChangeDutyCycle(3.5)
    pwm_X.ChangeDutyCycle(8.5)
    pwm_Z.ChangeDutyCycle(6.5)
    pwm_S.ChangeDutyCycle(10.3)
    time.sleep(1)
    
    pwm_Y.ChangeDutyCycle(0)
    pwm_X.ChangeDutyCycle(0)
    pwm_Z.ChangeDutyCycle(0)
    pwm_S.ChangeDutyCycle(0)
    
def angle_to_duty_cycle(angle=0):
    duty_cycle = (0.05 * PWM_FREQ) + (0.19 * PWM_FREQ * angle / 180)
    
    pwm_X.ChangeDutyCycle(2.5 + 10 * angle_X / 180)
        
    pwm_X.ChangeDutyCycle(2.5 + float(angle_X/10.0))
    return duty_cycle


step = 2.0

def Base(x):
    global angle_X
    
    if x <= -0.5:
        
        if angle_X + step < 170:
            angle_X += step
            print(angle_X)
        elif angle_X + step >=170:
            print(angle_X)
            pass
        
        pwm_X.ChangeDutyCycle(2.5 + 10 * angle_X / 180)
        
        return True
        
    elif x >= 0.5:
        
        if angle_X - step > 10:
            angle_X -= step
            print(angle_X)
        elif angle_X - step <= 10:
            print(angle_X)
            pass
        
        pwm_X.ChangeDutyCycle(2.5 + 10 * angle_X / 180)
        
        return True
    
    else:
        pwm_X.ChangeDutyCycle(0)
        return False
    
    
def control_Forward_Backward(x):
    global angle_Y

    if x <= -0.5:
        
        if angle_Y + step < 170:
            angle_Y += step
        elif angle_Y + step >=170:
            pass
        
        pwm_Y.ChangeDutyCycle(2.5 + 10 * angle_Y / 180)
        
        return True
        
    elif x >= 0.5:
        
        if angle_Y - step > 10:
            angle_Y -= step
        elif angle_Y - step <= 10:
            pass
        
        pwm_Y.ChangeDutyCycle(2.5 + 10 * angle_Y / 180)
        
        return True
    
    else:
        pwm_Y.ChangeDutyCycle(0)
        return False
    
    
def control_High_Low(but_Y,but_A):
    global angle_Z
    if but_Y == 1:
        if angle_Z < 170:
            angle_Z = angle_Z + 3
        elif angle_Z >= 170:
            pass
        
        pwm_Z.ChangeDutyCycle(2.5 + 10 * angle_Z / 180)       
        return True
    
    elif but_A == 1:
        if angle_Z > 10:
            angle_Z = angle_Z - 3
        elif angle_Z <= 10:
            pass
        
        pwm_Z.ChangeDutyCycle(2.5 + 10 * angle_Z / 180)
        
        
        return True
    
    elif but_A == 0 and but_Y == 0:
        pwm_Z.ChangeDutyCycle(0) 
        return False
    
    
stateS = 0
def control_Scissor(but_X,but_B):
    global state,stateS
    if but_X == 1 and but_B == 0 : 
        
        pwm_S.ChangeDutyCycle(2.5 + 10 * 0 / 180)
        #time.sleep(0.02)
        
        stateS = stateS + 1
        
        return True
    
    elif but_B == 1 and but_X == 0:
        pwm_S.ChangeDutyCycle(2.5 + 10 * 140 / 180)
        #time.sleep(0.02)
        stateS = stateS + 1
        
        return True
    
    elif but_B == 0 and but_X == 0:
        pwm_S.ChangeDutyCycle(0)
        stateS = 0
        return False
    
    
    
    

