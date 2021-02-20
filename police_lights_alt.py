import time
import blinkt
from utilities import set_strip

blinkt.set_brightness(0.1)
blinkt.set_clear_on_exit()

def police_lights_alt():
    count = 0
    while True:
        if count == 1 or count == 3 or count == 5:
            set_strip(blinkt, [[0, 0, 255],[0, 0, 0],[0, 0, 255],[0, 0, 0],[0, 0, 255],[0, 0, 0],[0, 0, 255],[0, 0, 0]])
        elif count == 7 or count == 9 or count == 11:
            set_strip(blinkt, [[0, 0, 0],[0, 0, 255],[0, 0, 0],[0, 0, 255],[0, 0, 0],[0, 0, 255],[0, 0, 0],[0, 0, 255]])
        else:
            blinkt.clear()

        count = count + 1

        if (count >= 13):
            count = 0

        blinkt.show()
        time.sleep(0.01)

police_lights_alt()
