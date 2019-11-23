from engine.GameObj import *
from engine.WindowManager import *
import time


class Renderer(object):

    def __init__(self, obj_dict: dict, window_manager: WindowManager):
        self.obj_dict = obj_dict
        self.window_manager = window_manager
        self.window = self.window_manager.get_window()
        self.canvas = self.window_manager.get_canvas()
        self.is_running = True
        self.FPS = 60

    def start_rendering(self):
        while self.is_running:
            self.canvas.delete("all")
            for game_obj_key in self.obj_dict:
                game_obj = self.obj_dict[game_obj_key]
                x = game_obj.loc[0]
                y = game_obj.loc[1]
                width = game_obj.width
                height = game_obj.height
                self.canvas.create_rectangle(x, y, x + width, y + height, fill="red")
            self.window.update()
            time.sleep(1 / self.FPS)
        self.window_manager.show_window()

    def stop(self):
        self.is_running = False
