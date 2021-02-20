# from graphics import *
import time
import json
import requests
# from fakeblinkt import Blinkt
from effects import (rainbow, rainbow_full, christmas_lights, police_lights,
fill_from_left, fill_from_right, scroll_from_left, scroll_from_right)
from utilities import reset
from random_blink import random_blink
# from random_fill import random_fill
import blinkt

def main():
    # blinkt = Blinkt()
    blinkt.set_clear_on_exit()
    blinkt.set_brightness(0.1)

    # win = GraphWin('Lights', 600, 150) # give title and dimensions
    # win.yUp() # make right side up coordinates!

    # win.setBackground("black")

    # for l in blinkt.lights:
    #    l.draw(win)

    # random_fill(blinkt)

    # rainbow_full(blinkt)
    # rainbow_full(blinkt)

    poll(blinkt)

    # for i in range(3):
    #     police_lights(blinkt)
    # reset(blinkt)

    # christmas_lights(blinkt)
    # reset(blinkt)

    # for _ in range(3):
    # fill_from_left(blinkt, 0, 0, 0, 200, 0, 100, 0.1)
    #     time.sleep(0.25)
    #     reset(blinkt)

    # for _ in range(3):
    #     fill_from_right(blinkt, 0, 0, 0, 0, 90, 100, 0.1)
    #     time.sleep(0.25)
    #     reset(blinkt)

    # for _ in range(3):
    #     scroll_from_left(blinkt, 0, 0, 0, 255, 165, 0, 0.1)
    # reset(blinkt)

    # for _ in range(3):
    #     scroll_from_right(blinkt, 0, 0, 0, 0, 255, 255, 0.1)
    # reset(blinkt)

    # rainbow(blinkt)

    # for a in range(120):
    #     lights[0].setFill(color_rgb(0, a*2, a*2))
    #     time.sleep(0.1)

    # win.getMouse()
    # win.close()

# Poll spreadsheet for command

def poll(blinkt):
    quit_requested = False
    while quit_requested == False:
        print("Polling...")
        cells = get_cells()
        print("Done")

        # Validate cells
        if "B1" not in cells or "B2" not in cells:
            print("Missing required data")
            time.sleep(5)
            continue

        cmd = cells["B1"]
        delay = float(cells["B2"])
        print("Cmd: " + cmd + ". Delay: " + str(delay))

        if (cmd == "0"):
            reset(blinkt)
            print("Quitting...")
            quit_requested = True
        elif (cmd == "1"):
            police_lights(blinkt)
            reset(blinkt)
        elif (cmd == "2"):
            christmas_lights(blinkt)
            reset(blinkt)
        elif (cmd == "3"):
            fill_from_left(blinkt, 0, 0, 0, 200, 0, 100, 0.1)
            reset(blinkt)
        elif (cmd == "4"):
            fill_from_right(blinkt, 0, 0, 0, 0, 90, 100, 0.1)
            reset(blinkt)
        elif (cmd == "5"):
            scroll_from_left(blinkt, 0, 0, 0, 255, 165, 0, 0.1)
            reset(blinkt)
        elif (cmd == "6"):
            scroll_from_right(blinkt, 0, 0, 0, 0, 255, 255, 0.1)
            reset(blinkt)
        elif (cmd == "7"):
            rainbow(blinkt)
            reset(blinkt)
        else:
            time.sleep(delay)

    print("Done")

def get_cells():
    j = requests.get('https://spreadsheets.google.com/feeds/cells/1NncutCH05S4NJTk_71p98TNo7pXz-zu3H8eGJWfJJJ4/1/public/full?alt=json')
    x = json.loads(j.text)

    cells = {}
    for e in x["feed"]["entry"]:
        cell = e["title"]["$t"]
        val = e["content"]["$t"]
        cells[cell] = val

    return cells

main()
