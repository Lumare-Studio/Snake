from engine import *
from Snakelauncher.SnakeGame import *
import multiprocessing
import threading
import copy


snake_core = SnakeGame()
window = snake_core.window
obj_manager = snake_core.obj_manager
snake_core_thread = threading.Thread(target=snake_core.main)
snake_core_thread.start()


render = Renderer(window_manager= window, dict_manager= obj_manager)
render_process = multiprocessing.Process(target=render.start_rendering())
render_process.start()






