from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import time
import pulseio
import touchio
import board
count = 0
increment = 1

lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16)


# create a Cap Touch value

touchA1 = touchio.TouchIn(A1.count)
touchA5 = touchio.TouchIn(A5.switch)

pastA1 = None
pastA5 = None

lcd.set_cursor_pos(0, 0)
lcd.print("Increment ")

lcd.set_cursor_pos(1,0)
lcd.print("Value ")

while True:
    while True:
    if touchA5.value and not(pastA5):
        print("Touched A5!")
        increment = increment*-1
        lcd.set_cursor_pos(0, 10)
        lcd.print(str(increment) + " ")
        print(increment)

    if touchA1.value and not(pastA1):
        print("Touched A1!")
        count = count + increment
        lcd.set_cursor_pos(1, 6)
        lcd.print("          ")
        # print 10 spaces to clear the past number
        lcd.set_cursor_pos(1, 6)
        lcd.print(str(count))
        print(count)
    pastA5 = touchA5.value
    pastA1 = touchA1.value
    time.sleep(.01)