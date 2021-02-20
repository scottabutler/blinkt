import random
import time

def random_fill(blinkt):
    count = 0
    while count < 200:
        r = random.randint(0, blinkt.NUM_PIXELS)
        print(r)
        blinkt.clear()
        for i in range(r):
            if i < 4:
                blinkt.set_pixel(i, 0, 255, 0)
            elif i < 6:
                blinkt.set_pixel(i, 255, 165, 0)
            else:
                blinkt.set_pixel(i, 255, 0, 0)

        blinkt.show()
        count += 1
        time.sleep(0.05)