from engine import *
from Snakelauncher.SnakeGame import *
import multiprocessing
import threading


snake_core = SnakeGame()
window = snake_core.window
obj_list = snake_core.obj_list
snake_core_thread = threading.Thread(target=snake_core.main)
snake_core_thread.start()

render = Renderer(obj_list, window)
render_process = multiprocessing.Process(target=render.start_rendering())
render_process.start()






