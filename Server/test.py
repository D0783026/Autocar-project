
#!/usr/bin/python
# -*- coding: utf-8-*-

import RPi.GPIO as GPIO
import curses
import time
from client import sent
while True:
     data = sent()
     print(data)

