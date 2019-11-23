from tkinter import *


class WindowManager(object):

    # constructor
    def __init__(self, window_name=None, window_width=0, window_height=0):
        # Make window
        self.window_name = window_name
        self.window_width = window_width
        self.window_height = window_height
        self.window = Tk()

        self.window.title(window_name)
        self.window.geometry(str(window_width) + "x" + str(window_height))
        # Add Canvas
        self.mainCanvas = Canvas(self.window, width=self.window_width, height=self.window_height)
        # Show window

    def get_window(self):
        return self.window

    def get_canvas(self):
        return self.mainCanvas

    def show_window(self):
        self.window.mainloop()
