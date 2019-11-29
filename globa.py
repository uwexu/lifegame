import tkinter as tk

#游戏参数
width = 60
height = 40
screen = []
delay = 1

#生命符号
black = '■'
white = '□'

#游戏窗体
window = tk.Tk()
window.title('world')
window.geometry('1000x600+200+100')

#游戏内容
text = tk.Text(window, width=width*2, height=height)
text.pack()

#列表转换成字符串
def transform(li):
    s = ''
    for l in li:
        for item in l:
            s = s + item
    return s


