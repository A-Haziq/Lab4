import socket
import time
from time import sleep

from hal import hal_led as led

def blink_led(delay):
    # Led Blink
    led.init()

    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)

def main:
