#Python 实现布朗运动
#Brownian motion -- an example of a multi-threaded Tkinter program

from tkinter import *
import random
import threading
import time
import sys


#画布（窗口）大小
WIDTH = 400
HEIGHT = 300


#设置布朗粒子（小球）的相关参数
SIGMA = 50              #小球的分散程度
BUZZ = 10               #小球的扩散速度
RADIUS = 2              #小球半径（大小）
LAMBDA = 50             #小球的运动速度
FILL = 'green'          #小球的颜色

stop = 0            # Set when main loop exits



def particle(canvas):
    
    r = RADIUS
    x = random.gauss(WIDTH/2.0, SIGMA)          #随机生成符合高斯分布的随机数，WIDTH/2.0和SIGMA为高斯分布的两个参数
    y = random.gauss(HEIGHT/2.0, SIGMA)
    p = canvas.create_oval(x-r, y-r, x+r, y+r, fill = FILL)

    while not stop:

        dx = random.gauss(0, BUZZ)
        dy = random.gauss(0, BUZZ)
        dt = random.expovariate(LAMBDA)

        try:
            canvas.move(p, dx, dy)

        except TclError:
            break

        time.sleep(dt)


def main():     #主函数
    
    global stop
    root = Tk()
    canvas = Canvas(root, width = WIDTH, height = HEIGHT)
    canvas.pack(fill = 'both', expand = 1)

    #粒子数目
    np = 30

    if sys.argv[1:]:
        np = int(sys.argv[1])
        
    for i in range(np):
        t = threading.Thread(target = particle, args = (canvas,))
        t.start()

    try:
        root.mainloop()

    finally:
        stop = 1



main()
