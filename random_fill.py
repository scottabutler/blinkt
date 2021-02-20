import random
import time
import blinkt

blinkt.set_clear_on_exit()
blinkt.set_brightness(0.05)

def random_fill():
    count = 0
    while True: # count < 200:
        r = random.randint(0, blinkt.NUM_PIXELS)
        # print(r)
        blinkt.clear()
        for i in range(r):
            if i < 4:
                blinkt.set_pixel(i, 0, 255, 0)
            elif i < 6:
                blinkt.set_pixel(i, 255, 165, 0)
            else:
                blinkt.set_pixel(i, 255, 0, 0)

        blinkt.show()
        # count += 1
        time.sleep(0.07)

random_fill()
