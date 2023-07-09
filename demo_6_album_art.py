from picographics import PicoGraphics, DISPLAY_COSMIC_UNICORN as DISPLAY
display = PicoGraphics(display=DISPLAY)
from cosmic import CosmicUnicorn
# from galactic import StellarUnicorn

import jpegdec

gu = CosmicUnicorn()

gu.set_brightness(0.75)
 
WIDTH, HEIGHT = display.get_bounds()

filename = "kev.jpg"

j = jpegdec.JPEG(display)

# Open the JPEG file
j.open_file(filename)
x = 0
y = 0
width = WIDTH 
height = HEIGHT

# find the middle of the display and take from the middle of the image
center = (WIDTH // 2) - (240 // 2)

# Decode the JPEG
j.decode(x, y, jpegdec.JPEG_SCALE_EIGHTH, dither=True)
gu.update(display)
