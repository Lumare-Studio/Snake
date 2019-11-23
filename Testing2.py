from engine import *
from tkinter import *


# Constant fields
WIDTH = 800
HEIGHT = 800
SPEED = 25
OBJECT_WIDTH = 25

snake = None


def move_snake(key):
    print(key)
    if key == "Left":
        snake.velocity = [-SPEED, 0]
    elif key == "Right":
        snake.velocity = [SPEED, 0]
    elif key == "Down":
        snake.velocity = [0, SPEED]
    elif key == "Up":
        snake.velocity = [0, -SPEED]


window = WindowManager("Testing", 800, 800)


def get_user_input(event):
    a = event.keycode
    print(a)


window.window.bind_all('<KeyPress>', get_user_input)
canvas = window.get_canvas()
rectangle = canvas.create_rectangle(0, 0, 25, 25, fill="red")
canvas.pack()
window.show_window()
