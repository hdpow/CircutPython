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
cap_touch_black = board.A3
cap_touch_red = board.A1
touchBlack = touchio.TouchIn(cap_touch_black)
touchRed = touchio.TouchIn(cap_touch_red)

pastBlack = None
pastRed = None

lcd.set_cursor_pos(0, 0)
lcd.print("Increment ")

lcd.set_cursor_pos(1,0)
lcd.print("Value ")

while True:
    if touchBlack.value and not(pastBlack):
        print("Touched Black!")
        increment = increment*-1
        lcd.set_cursor_pos(0, 10)
        lcd.print(str(increment) + " ")
        print(increment)

    if touchRed.value and not(pastRed):
        print("Touched Red!")
        count = count + increment
        lcd.set_cursor_pos(1, 6)
        lcd.print("          ")
        # print 10 spaces to clear the past number
        lcd.set_cursor_pos(1, 6)
        lcd.print(str(count))
        print(count)
    pastBlack = touchBlack.value
    pastRed = touchRed.value
    time.sleep(.01)
    