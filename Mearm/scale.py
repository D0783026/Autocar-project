from tkinter import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# GPIO.setup(26, GPIO.OUT)
# pwm = GPIO.PWM(26, 100)
# pwm.start(5)

class App:
	
    def __init__(self, master, pin_no1):
        GPIO.setup(pin_no1, GPIO.OUT)
        self.pwm = GPIO.PWM(pin_no1,100)
        self.pwm.start(0)
        frame = Frame(master)
        frame.pack()
        scale = Scale(frame, from_=0, to=180, 
              orient=HORIZONTAL, command=self.update)
        scale.grid(row=0)


    def update(self, angle):
        duty = float(angle) / 10.0 + 2.5
        self.pwm.ChangeDutyCycle(duty)

root = Tk()

root.wm_title('Servo Control')
app = App(root,6)
app1 = App(root,5)
app2 = App(root,23)
app3 = App(root,22)
root.geometry("200x200+0+0")
root.mainloop()
