import time
from time import sleep

from hal import hal_led as led
from hal import hal_input_switch as switch_init
from hal import hal_input_switch as read_slide_switch

def blink_led(delay):
    # Led Blink
    led.init()

    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)

def main():

    led.init()
    switch_init()

    delay = 0.1

    while True:
        if read_slide_switch() == 0:
            blink_led(delay)
        else:
            led.set_output(0, 0)
            time.sleep(0.1)

if __name__ == "__main__":
    main()