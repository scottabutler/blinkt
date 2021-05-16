import time

def loop(running):
    i = 0
    while (i < 20 and running == True):
        print("running {0} {1}".format(i, running))
        time.sleep(.5)
        i += 1