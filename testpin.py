import time
import RPi.GPIO as GPIO

def show(pin):
    if GPIO.input(pin):
        return 1
    else:
        return 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.IN)
GPIO.setup(35, GPIO.IN)
GPIO.setup(32, GPIO.IN)
GPIO.setup(33, GPIO.IN)
GPIO.setup(36, GPIO.IN)

while True:
    if show(38) == 1:
        print "pin38 ON\n"
    if show(38) == 0:
        print "pin38 OFF\n"
    if show(40) == 1:
        print "pin40 ON\n"
    if show(40) == 0:
        print "pin40 OFF\n"
    if show(32) == 1:
        print "pin32 ON\n"
    if show(32) == 0:
        print "pin32 OFF\n"
    if show(35) == 1:
        print "pin35 ON\n"
    if show(35) == 0:
        print "pin35 OFF\n"
    if show(36) == 1:
        print "pin36 ON\n"
    if show(36) == 0:
        print "pin36 OFF\n"
    time.sleep(1)
