import json
import requests
import time
import blinkt
from utilities import set_strip

def main():
    quit_requested = False
    while quit_requested == False:
        cells = get_cells()

        # Validate cells
        if "B1" not in cells or "B2" not in cells:
            print("Missing required data")
            time.sleep(5)
            continue

        cmd = cells["B1"]
        delay = float(cells["B2"])
        print("Cmd: " + cmd + ". Delay: " + str(delay))

        if (cmd == "0"):
            print("Quitting...")
            quit_requested = True
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

def main_seq():
    cells = get_sequence_cells()
    # print(cells)
    for c in cells:
        rgbs = []
        x = c.split("|")
        delay = x.pop()
        for i in x:
            y = i.split(",")
            rgbs.append([int(y[0]), int(y[1]), int(y[2])])

        print(rgbs)
        blinkt.clear()
        for j in rgbs:
            set_strip(blinkt, rgbs[j])
        # for p in range(8): #  blinkt.NUM_PIXELS:
            # blinkt.set_pixel(p, rgbs[p][0], rgbs[p][1], rgbs[p][2])
            # print(rgbs[p][0])

        blinkt.show()
        time.sleep(float(delay))
    print("Done")

def get_sequence_cells():
    j = requests.get('https://spreadsheets.google.com/feeds/cells/1NncutCH05S4NJTk_71p98TNo7pXz-zu3H8eGJWfJJJ4/2/public/full?alt=json')
    x = json.loads(j.text)

    cells = []
    for e in x["feed"]["entry"]:
        val = e["content"]["$t"]
        if "|" in val:
            cells.append(val)

    return cells

main_seq()