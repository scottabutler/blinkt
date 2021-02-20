import json
import requests
import time

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

main()