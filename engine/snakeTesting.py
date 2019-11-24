import multiprocessing
import threading

from engine import *
import time

OBJECT_WIDTH = 25
OBJECT_HEIGHT = 25
WIDTH = 800
HEIGHT = 800
obj_list = dict()
snake = Snake()

def populate_snake():
    for i in range (10):
        location = [WIDTH / 2 + i * OBJECT_WIDTH, HEIGHT / 2 ]
        body = GameObj(location=location, width=OBJECT_WIDTH, height=OBJECT_WIDTH, tag="snake")
        snake.insert(body)
        location = (location[0], location[1])
        obj_list[location] = body
        time.sleep(1)


# create window
title = "Snake Test"
window_width = 800
window_height = 800
window_manager = WindowManager(title, window_width, window_height)

# populate square
populate_thread = threading.Thread(target= populate_snake)
populate_thread.start()


# start rendering
renderer = Renderer(obj_list, window_manager)
render_process = multiprocessing.Process(target=renderer.start_rendering())
render_process.start()
render_process.join()

