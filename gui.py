import os
import pyautogui as pg
import datetime
import signal
import time
import threading


def shot():
    pg.moveTo(500, 1600)
    # print(pg.size())
    # pg.click()
    # pg.click(button="left", clicks=3, interval=0.5)
    dt_now = datetime.datetime.now()
    screen_shot = pg.screenshot()
    screen_shot.save('screen_shot/'+ str(dt_now.hour) +str(dt_now.second) + str(dt_now.microsecond) + '.png')

def setting_condition():
    pg.click()
    pg.click(button="left", clicks=3, interval=0.5)
    pg.press("down")



def scheduler(interval, f, wait = True):
    base_time = time.time()
    next_time = 0
    while True:
        t = threading.Thread(target = f)
        t.start()
        if wait:
            t.join()
        next_time = ((base_time - time.time()) % interval) or interval
        time.sleep(next_time)
        setting_condition()

scheduler(1, shot, False)
 