from tkinter import *

class WindowManager(object):

    #constructor
    def __init__(self, windowName = None, windowWidth = 0, windowHeight = 0):
        # Make window
        self.windowName = windowName
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.window = Tk()
        self.window.title(self.windowName)
        self.window.geometry(str(self.windowHeight) + 'x' + str(self.windowWidth))
        # Add canvas
        self.mainCanvas = Canvas(self.window, width = self.windowWidth, height = self.windowHeight)
        # Show window
        self.window.mainloop()

    def getWindow(self):
        return self.window

    def getCanvas(self):
        return self.mainCanvas
