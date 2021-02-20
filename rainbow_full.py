import blinkt
import time
import colorsys

def rainbow_full():
    spacing = 360.0 / 16.0
    hue = 0

    count = 0
    while True: # count < 360:
        hue = count # int(time.time() * 100) % 360
        offset = 0 #  * spacing
        h = ((hue + offset) % 360) / 360.0
        r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]

        for x in range(blinkt.NUM_PIXELS):
            blinkt.set_pixel(x, r, g, b)

        blinkt.show()
        count = count + 1
	if (count >= 360):
		count = 0
        time.sleep(0.025)

blinkt.set_clear_on_exit()
blinkt.set_brightness(0.05)

rainbow_full()
