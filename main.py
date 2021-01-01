import time

import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
 
import board
import busio
import adafruit_us100
uart = busio.UART(board.TX, board.RX, baudrate=9600)
us100 = adafruit_us100.US100(uart)00 = adafruit_us100.US100(uart)
 
while True:
    now=time.monotonic
    if sonar.distance <= 25:
        try:
            
            print((sonar.distance,))
        except RuntimeError:
            print("Retrying!")
    else:
        print("25")

