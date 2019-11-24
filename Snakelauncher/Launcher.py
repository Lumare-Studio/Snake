from engine import *
from Snakelauncher import SnakeGame
import multiprocessing
import threading


def launcher():
    snake_core = SnakeGame()
    window = snake_core.window
    obj_list = snake_core.obj_list
    snake_core_thread = threading.Thread(target=snake_core.main)

    render = Renderer(obj_list, window)
    render_process = multiprocessing.Process(target=render.start_rendering())
    snake_core_thread.start()
    render_process.start()


launcher()




