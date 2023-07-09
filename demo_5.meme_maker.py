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
text_scale = 3

# find the middle of the display and take from the middle of the image
center = (WIDTH // 2) - (240 // 2)

white = display.create_pen(255,255,255)

# Decode the JPEG
j.decode(center, y, jpegdec.JPEG_SCALE_FULL, dither=False)
display.set_pen(white)

text = "Robot Maker"
spacing = 1
fixed_width = False

# you an measure the length of text in pixel, useful for positioning
text_width = display.measure_text(text, text_scale, spacing, fixed_width)

text_center = (WIDTH // 2) - (text_width //2)
print(f"text_width: {text_width}, text_center: {text_center}")

display.text(text, text_center, y+height - 20, WIDTH, text_scale)
display.update()
