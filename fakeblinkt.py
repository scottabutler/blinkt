from graphics import *

class Blinkt:
    NUM_PIXELS = 8

    def __init__(self):
        lights = []
        for x in range(self.NUM_PIXELS):
            c = Circle(Point(60+ (60*x),100), 25)
            c.setOutline("#ccc")
            lights.append(c)
        self.lights = lights

    def set_pixel(self, x, r, g, b):
        self.lights[x].setFill(color_rgb(r, g, b))

    def set_all(self, r, g, b):
        for i in range(self.NUM_PIXELS):
            self.set_pixel(i, r, g, b)

    def clear(self):
        self.set_all(0, 0, 0)

    def show(self):
        pass
        # print('Show')

    def set_clear_on_exit(self):
        pass
        # print('Clear on exit')

    def set_brightness(self, b):
        pass
        # print('Set brightness to ' + str(b))