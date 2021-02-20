import time

def reset(blinkt):
    blinkt.set_all(0, 0, 0)
    blinkt.show()
    time.sleep(0.5)

def set_strip(blinkt, values):
    for i in range(blinkt.NUM_PIXELS):
        blinkt.set_pixel(i, values[i][0], values[i][1], values[i][2])