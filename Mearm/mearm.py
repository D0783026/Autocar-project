import RPi.GPIO as GPIO
import time
import curses
 
CONTROL_PIN = 14
PWM_FREQ = 50
STEP=1
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(CONTROL_PIN, GPIO.OUT)
 
pwm = GPIO.PWM(CONTROL_PIN, PWM_FREQ)
pwm.start(0)
stdrc = curses.initscr()
stdrc.clear()
def angle_to_duty_cycle(angle=0):
    duty_cycle = (0.05 * PWM_FREQ) + (0.19 * PWM_FREQ * angle / 180)
    return duty_cycle




if __name__ == '__main__':
    angle=0
    
    while True:
        angle+=1
        ch = stdrc.getkey()
        if ch=='a':
            dc = angle_to_duty_cycle(angle) 
            pwm.ChangeDutyCycle(dc)
            print('角度={: >3}, 工作週期={:.2f}'.format(angle, dc))
            
               

    pwm.stop()
    GPIO.cleanup()