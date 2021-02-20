import time
import colorsys
from utilities import set_strip, reset

def fill_from_left(blinkt, baseR, baseG, baseB, r, g, b, delay):
    blinkt.set_all(baseR, baseG, baseB)
    blinkt.show()
    for i in range(blinkt.NUM_PIXELS):
        blinkt.set_pixel(i, r, g, b)
        blinkt.show()
        time.sleep(delay)

def fill_from_right(blinkt, baseR, baseG, baseB, r, g, b, delay):
    blinkt.set_all(baseR, baseG, baseB)
    blinkt.show()
    count = len(blinkt.lights)
    for i in range(blinkt.NUM_PIXELS):
        blinkt.set_pixel(count-i-1, r, g, b)
        blinkt.show()
        time.sleep(delay)

def scroll_from_left(blinkt, baseR, baseG, baseB, r, g, b, delay):
    for i in range(blinkt.NUM_PIXELS):
        blinkt.set_all(baseR, baseG, baseB)
        blinkt.set_pixel(i, r, g, b)
        blinkt.show()
        time.sleep(delay)

def scroll_from_right(blinkt, baseR, baseG, baseB, r, g, b, delay):
    count = len(blinkt.lights)
    for i in range(blinkt.NUM_PIXELS):
        blinkt.set_all(baseR, baseG, baseB)
        blinkt.set_pixel(count-i-1, r, g, b)
        blinkt.show()
        time.sleep(delay)

def rainbow(blinkt):
    spacing = 360.0 / 16.0
    hue = 0

    count = 0
    while count < 255:
        hue = int(time.time() * 100) % 360
        for x in range(len(blinkt.lights)):
            offset = x * spacing
            h = ((hue + offset) % 360) / 360.0
            r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
            blinkt.set_pixel(x, r, g, b)

        blinkt.show()
        count = count + 1
        time.sleep(0.001)

def rainbow_full(blinkt):
    spacing = 360.0 / 16.0
    hue = 0

    count = 0
    while count < 360:
        hue = count # int(time.time() * 100) % 360
        offset = 0 #  * spacing
        h = ((hue + offset) % 360) / 360.0
        r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]

        for x in range(len(blinkt.lights)):
            blinkt.set_pixel(x, r, g, b)

        blinkt.show()
        count = count + 1
        time.sleep(0.025)

def christmas_lights(blinkt):
    count = 0
    index = 1
    while count < 10:
        if index == 1:
            set_strip(blinkt, [[30, 90, 247],[0, 0, 0],[57, 242, 138],[0, 0, 0],[30, 90, 247],[0, 0, 0],[57, 242, 138],[0, 0, 0]])
        elif index == 2:
            set_strip(blinkt, [[0, 0, 0],[238, 65, 63],[0, 0, 0],[255, 217, 34],[0, 0, 0],[238, 65, 63],[0, 0, 0],[255, 217, 34]])
        else:
            set_strip(blinkt, [[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0]])

        index = index + 1
        if index >= 3:
            index = 1
        count = count + 1

        blinkt.show()
        time.sleep(0.5)

def police_lights(blinkt):
    count = 0
    while count < 12:
        if count == 1 or count == 3:
            set_strip(blinkt, [[0, 0, 255],[0, 0, 255],[0, 0, 255],[0, 0, 255],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0]])
        elif count == 6 or count == 8:
            set_strip(blinkt, [[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[255, 0, 0],[255, 0, 0],[255, 0, 0],[255, 0, 0]])
        else:
            blinkt.clear()

        count = count + 1

        blinkt.show()
        time.sleep(0.07)