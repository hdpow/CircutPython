import board
import neopixel
import time
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
while true:
  print("Make it red!")
  dot.fill((255,0,0))
  time.sleep(.5)
  print("make it yellow!")
  time.sleep(.5)
    dot.fill((255,255,0))

  
