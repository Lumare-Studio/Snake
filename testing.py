import time

from engine.WindowManager import *

a = WindowManager("Testing", 800, 800)
w = a.get_window()
c = a.get_canvas()
x = 0
y = 0
hi = 50
wi = 50
square = c.create_rectangle(x, y, x + hi, y + wi, fill="red")
i = 0
while True:
    print("move", i)
    c.delete("all")
    x += 10
    square = c.create_rectangle(x, y, x + hi, y + wi, fill="red")
    print(x, " ", y)
    if x > 800:
        x = 0
        y += 10
    if y > 800:
        y = 0
    w.update()
    time.sleep(0.1)
    i += 1

a.show_window()
