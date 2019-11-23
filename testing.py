import multiprocessing
import time
import threading

from engine.WindowManager import *
from engine.Renderer import *


class populator(object):
    def __init__(self, game_obj_dict: dict):
        self.game_obj_dict = game_obj_dict

    def populate(self):
        for i in range(10):
            location = (i * 100, i * 100)
            velocity = [0, 0]
            tag = "Snake"
            width = 100
            height = 100
            game_obj = GameObj(location, velocity, [0, 0], tag, width, height)
            game_obj_dict[location] = game_obj
            time.sleep(1)


# create gameobj
game_obj_dict = dict()

# create window
title = "Render Test"
window_width = 800
window_height = 800
window_manager = WindowManager(title, window_width, window_height)

# populate square
print("start populate")
populate_populator = populator(game_obj_dict)
populate_thread = threading.Thread(target=populate_populator.populate)
populate_thread.start()

# start rendering
renderer = Renderer(game_obj_dict, window_manager)
render_process = multiprocessing.Process(target=renderer.start_rendering())
render_process.start()
render_process.join()
