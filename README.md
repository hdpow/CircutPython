# CircutPython

### Description

basically a copy of alden's code, found [here](https://github.com/adent11/CircuitPython/blob/master/HelloCircuitPython.py). In essence, there is one variable, x. the variable x directly relates to the level of "blue" in the Neopixel. the opposite of that, plus 255, is the "red" level.  if the level is greater than 195, it goes down. if it is greater than 60, it goes up. I edited it a bit so that it would less pure color, and more of the gradient.

### Evidence

```python
import board
import neopixel
import time
x = 0
change = 1

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

while True:
    if x > 195:
        up = -1
    if x < 60:
        up = 1
    x += up
    dot.fill((-x+255, 0, x))
    time.sleep(.01)
    print("Red Level: ", -x+255)
    print("Blue Level:", x)
    
```
### Images
https://im5.ezgif.com/tmp/ezgif-5-e7c2673df54b.gif

### Reflect
this assignment was pretty cool. as a professional epic gamer, everything that I own has to be dripping in RGB, so i really liked this assignment. It was a really good intro to circut python.

# CircutPython Servo


### Description

The CircutPython Servo involves utilizing the Capacitive Touch module to modify a variable that then modifies a servo. if one wire is touched, the angle of the servo is set to zero. if the other wire is touched, the angle is set to 180.

### Evidence

```python
import board
import time
import servo
import pulseio
import touchio

# create a PWMOut object on Pin A2.
pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
 
# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

# create a Cap Touch value
touch_A4 = touchio.TouchIn(board.A4)
touch_A5 = touchio.TouchIn(board.A5)

while True:
    print("This works!")
    if touch_A4.value:
        my_servo.angle = 0
        print("Touched A4!")
    if touch_A5.value:
        my_servo.angle = 180
        print("Touched A5!")
    time.sleep(0.05)
 ```

### Proof

[<img src="/Images/CircutPythonServo.gif" alt="CircutPythonServo.gif" width="350" height="250">](/Images/CircutPythonServo.gif)

### Reflect

This assignment was very interesting. the capacative touch is very satisfying to work with. I had some troubles with the library and figuring out how it worked, but it turned out that the circutpy had some left over librarys from the previous owner and I didnt need them, so i simply deleted everything exept for the servo.

# CircutPython LCD

### Discription

Remember that assignment from Engineering 2 where you wired up an LCD screen, a button, and a switch?  The LCD screen displayed the button press count and the switch determined if you were counting up or down.  Let's see if we can spice that up a little for Engineering 3 using CircuitPython.

### Process

well, this was a fun assignment. Thank god that other people can tell me what code I have to use special thanks to [Bob](https://github.com/jkammau97/CircuitPython) for literally carrying me. By far the most difficult part of the assignment was figuring out how to make a button that does not repeat constantly. and... I never really figured it out. I have a vauge idea of how bob's code works. It has something to do with the fact that, on the last line, it says

``` python
    pastBlack = touchBlack.value
    pastRed = touchRed.value
```
I think that this makes it so that after it does the function once, it makes the value of touch(colour).value None once the function is done once. the value stays at None untill the wire is touched again, changing it to True for one tick before it changes into None again. this is caused by the code
``` python
    if touch(colour.value and not(past(colour):
```

### Evidence

Heres the code working:

[<img src="/Images/CircutPythonLCD.gif" alt="CircutPythonLCD.gif" width="350" height="250">](/Images/CircutPythonLCD.gif)

Heres a wiring diagram, borrowed from [Alden](https://github.com/adent11/CircuitPython#CircuitPython-LCD)

My code can be found [here](https://github.com/hdpow/CircutPython/blob/main/main.py)

bob's code can be found [here](https://github.com/jkammau97/CircuitPython)

### Reflection

once again, it was really hard for me to summon the mental energy to actually do this assigment. once I started and broke down my inhebitions abut borrowning other peoples advice and work, It sped up a lot. I think I know more about true/false/null, and I know how to make a button that only sends a signal once. so all in all, pretty successfull.
