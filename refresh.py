import _thread
import random
import time
import rule
from globa import *


#模拟繁殖
def isdeath(i, j):
    global screen
    count = 0
    left = white
    right = white
    up = white
    down = white

    left_up = white
    left_down = white
    right_up = white
    right_down = white
    try:
        left = screen[i][j-1]
        right = screen[i][j+1]
        up = screen[i-1][j]
        down = screen[i+1][j]

        left_up = screen[i-1][j-1]
        left_down = screen[i-1][j+1]
        right_up = screen[i+1][j-1]
        right_down = screen[i+1][j+1]
    except:
        pass

    if left == black:
        count = count + 1
    if right == black:
        count = count + 1
    if up == black:
        count = count + 1
    if down == black:
        count = count + 1

    if left_up == black:
        count = count + 1
    if left_down == black:
        count = count + 1
    if right_up == black:
        count = count + 1
    if right_down == black:
        count = count + 1

    return rule.rule_reproduce_classic(count)


#模拟生存
def islive(i, j):
    global screen
    count = 0
    left = white
    right = white
    up = white
    down = white

    left_up = white
    left_down = white
    right_up = white
    right_down = white
    try:
        left = screen[i][j - 1]
        right = screen[i][j + 1]
        up = screen[i - 1][j]
        down = screen[i + 1][j]

        left_up = screen[i-1][j-1]
        left_down = screen[i-1][j+1]
        right_up = screen[i+1][j-1]
        right_down = screen[i+1][j+1]
    except:
        pass

    if left == black:
        count = count + 1
    if right == black:
        count = count + 1
    if up == black:
        count = count + 1
    if down == black:
        count = count + 1

    if left_up == black:
        count = count + 1
    if left_down == black:
        count = count + 1
    if right_up == black:
        count = count + 1
    if right_down == black:
        count = count + 1

    return rule.rule_survive_classic(count)


def get_screen():
    global screen
    new_screen = []
    for i in range(0, height):
        line = []
        for j in range(0, width):
            if screen[i][j] == black:
                line.append(islive(i, j))
            else:
                line.append(isdeath(i, j))
        new_screen.append(line)
    screen.clear()
    screen = new_screen.copy()

def refresh_screen():
    while True:
        time.sleep(delay)
        get_screen()
        text.delete('1.0', 'end')
        text.insert(tk.INSERT, transform(screen))
        print(screen)


def start():
    _thread.start_new_thread(refresh_screen, ())

