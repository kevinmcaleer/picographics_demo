import time
import math
import machine
from stellar import StellarUnicorn
from picographics import PicoGraphics, DISPLAY_STELLAR_UNICORN as DISPLAY

# overclock to 200Mhz
machine.freq(200000000)

# create stellar object and graphics surface for drawing
stellar = StellarUnicorn()
graphics = PicoGraphics(DISPLAY)

brightness = 0.5

yellow = graphics.create_pen(255,255,0)
cyan = graphics.create_pen(0,255,255)
red = graphics.create_pen(255,0,0)

graphics.set_pen(red)
x = 1
y = 1
width = 10
height = 10
graphics.rectangle(x,y,width,height)
stellar.update(graphics)
