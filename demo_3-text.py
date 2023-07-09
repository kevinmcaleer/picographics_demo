from gfx_pack import GfxPack
graphics = GfxPack()
display = graphics.display

WIDTH, HEIGHT = display.get_bounds()
display.set_backlight(0.5)

display.set_pen(0)  # Set pen to white
display.clear()
display.set_pen(15) # set the pen to black

scale = 2 # change this to see what happens
x = 0
y = 0

display.text("Hello World", x, y, WIDTH, scale)
display.update()
