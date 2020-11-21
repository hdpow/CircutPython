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
