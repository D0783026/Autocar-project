import RPi.GPIO as GPIO
import time
from getkey import getkey,keys

CONTROL_PIN = 17
PWM_FREQ = 50
STEP=1
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(CONTROL_PIN, GPIO.OUT)
 
pwm = GPIO.PWM(CONTROL_PIN, PWM_FREQ)
pwm.start(0)
 
def angle_to_duty_cycle(angle=0):
    duty_cycle = (0.05 * PWM_FREQ) + (0.19 * PWM_FREQ * angle / 180)
    return duty_cycle
 
try:
    print('按下 Ctrl-C 可停止程式')
    while True:
        key = getkey()
        angle = 0
        if key == keys.UP and angle < 180:
            angle = angle + STEP
            dc = angle_to_duty_cycle(angle)
            pwm.ChangeDutyCycle(dc)
            print('角度={: >3}, 工作週期={:.2f}'.format(angle, dc))
        elif key == keys.DOWN and angle < 180:
            angle = angle - STEP
            dc = angle_to_duty_cycle(angle)
            pwm.ChangeDutyCycle(dc)
            print('角度={: >3}, 工作週期={:.2f}'.format(angle, dc))
except KeyboardInterrupt:
    print('關閉程式')
finally:
    pwm.stop()
    GPIO.cleanup()