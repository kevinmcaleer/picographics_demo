from picographics import PicoGraphics, PEN_P8, DISPLAY_PICO_DISPLAY_2 as DISPLAY
display = PicoGraphics(display=DISPLAY)

import jpegdec


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

# clipping can crop an image
display.set_clip(x, y, width, height)

# Decode the JPEG
j.decode(center, y, jpegdec.JPEG_SCALE_FULL, dither=False)
display.update()