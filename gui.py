import os
import pyautogui as pg
import datetime
import signal
import time
import threading

place_list = [
    "RJCO",
    "RJCC",
    "RJNA",
    "RJGG",
    "RJFU",
    "RJDA",
    "RJOC",
    "RJOH",
    "RJOY",
    "RJBE",
    "RJFF",
    "RJSF"
]

visibility =[
    20,
    30,

]

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

def positioning():
    while True:
        x=input("取得したい箇所にカーソルを当てEnterキー押してください\n")
        print(pg.position())

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

def beforeFlight(place,visib):
    pg.moveTo(-3732, 4, 2) #フライトタブ
    pg.click()
    pg.moveTo(-3732, 41, 2) #フライト設定
    pg.click()
    pg.moveTo(-2214, 344, 2) #場所変更
    pg.click()
    pg.moveTo(-2454, 126, 2) #場所検索ボックス
    pg.click()

    for i in range(10):
        pg.press("backspace")
    pg.write(place)
    pg.press("enter") #場所入力

    pg.moveTo(-2183, 560, 2) #気象カスタマイズ
    pg.click()
    pg.moveTo(-2150, 117, 2) #視程
    pg.click()
    for i in range(10):
        pg.press("backspace")
    pg.write(visib)
    pg.press("enter") #場所入力


    pg.moveTo(-2188, 977, 2) #実行完了
    pg.click()
    pg.moveTo(-2188, 1044, 2) #新規フライト
    pg.click()
    pg.moveTo(-2756, 674, 2) #フライト開始
    pg.click()
    pg.moveTo(-2606, 690, 2) #了解
    pg.click()


# scheduler(1, shot, False)

beforeFlight("NAHA", 20)


# positioning()

 