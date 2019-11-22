from engine.WindowManager import *

a = WindowManager("Testing", 500, 500)
c = a.get_canvas()
r = c.create_rectangle(0, 0, 30, 30, fill="red")
c.pack()
a.show_window()
