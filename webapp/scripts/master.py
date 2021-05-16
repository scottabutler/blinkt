import threading
import time
import task

def doit(arg):
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        print ("working on %s" % arg)
        time.sleep(1)
    print("Stopping as you wish.")

def runTask(arg):
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        print ("working on %s" % arg)
        task.loop(getattr(t, "do_run", True))
        time.sleep(1)

def main():
    # t = threading.Thread(target=doit, args=("task",))
    t = threading.Thread(target=runTask, args=("task",))
    t.start()
    time.sleep(5)
    print('stopping')
    t.do_run = False
    t.stop()
    print('stopped')


if __name__ == "__main__":
    main()