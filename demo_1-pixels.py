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
graphics.set_pen(yellow)
graphics.pixel(1,1)
graphics.set_pen(red)
graphics.pixel(2,1)
graphics.set_pen(cyan)
graphics.pixel(3,1)
stellar.update(graphics)
