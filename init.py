import random
from globa import *

#初始化地图
def init():
    for i in range(height):
        line = []
        for j in range(width):
            if random.random() > 0.8:
                line.append(black)
            else:
                line.append(white)
        screen.append(line)
    text.insert(tk.INSERT, transform(screen))