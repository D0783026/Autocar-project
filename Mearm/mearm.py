import RPi.GPIO as GPIO
import time
 
CONTROL_PIN = 14
PWM_FREQ = 50
STEP=1
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(CONTROL_PIN, GPIO.OUT)
 
pwm = GPIO.PWM(CONTROL_PIN, PWM_FREQ)
pwm.start(90)
 
def angle_to_duty_cycle(angle=0):
    duty_cycle = (0.05 * PWM_FREQ) + (0.19 * PWM_FREQ * angle / 180)
    return duty_cycle




if __name__ == '__main__':
    flag=0
    ch = input()
    while True:
        if ch=='j':
            for angle in range(90,180,STEP):
                if ch=='p':
                    print('結束程式')
                    flag=1
                    break
                dc = angle_to_duty_cycle(angle)
                pwm.ChangeDutyCycle(dc)
                print('角度={: >3}, 工作週期={:.2f}'.format(angle, dc))
                time.sleep(0.5)
        elif ch=='l':
            for angle in range(90,-1,STEP):
                if ch=='p':
                    print('結束程式')
                    flag=1
                    break
                dc = angle_to_duty_cycle(angle) 
                pwm.ChangeDutyCycle(dc)
                print('角度={: >3}, 工作週期={:.2f}'.format(angle, dc))
                time.sleep(0.5)
               
        if flag==0:
            break;

    pwm.stop()
    GPIO.cleanup()