def run():
    try:
        import time
        import blinkt

        blinkt.set_brightness(0.1)
        blinkt.set_clear_on_exit()

        for a in range(3):
            for x in range(blinkt.NUM_PIXELS):
                blinkt.set_pixel(x, 0, 150, 0)

            blinkt.show()
            time.sleep(0.25)
            blinkt.clear()
            blinkt.show()
            time.sleep(0.25)
    except:
        print("Something went wrong in the startup script")
