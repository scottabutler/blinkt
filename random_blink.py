import random
import time

def random_blink(blinkt):
    while True:
        pixels = random.sample(range(blinkt.NUM_PIXELS), random.randint(1, 5))
        # for i in range(blinkt.NUM_PIXELS):
        #     if i in pixels:
        #         blinkt.set_pixel(i, 255, 150, 0)
        #     else:
        #         blinkt.set_pixel(i, 0, 0, 0)
        for i in range(blinkt.NUM_PIXELS):
            blinkt.set_pixel(i, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        blinkt.show()
        time.sleep(0.25)