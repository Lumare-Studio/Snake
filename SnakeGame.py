from engine import *


# Constant fields
WIDTH = 800
HEIGHT = 800
SPEED = 25
OBJECT_WIDTH = 25


# Set up Window
a = WindowManager("Testing", 800, 800)
c = a.get_canvas()
r = c.create_rectangle(0, 0, 25, 25, fill="red")
c.pack()
a.show_window()

snake = None


def reset():
    snake = Snake()
    snake.insert(GameObj(location=[WIDTH / 2 + 2 * OBJECT_WIDTH, HEIGHT/2], tag="snake"))
    snake.insert(GameObj(location=[WIDTH / 2 + OBJECT_WIDTH, HEIGHT / 2], tag="snake"))
    snake.insert(GameObj(location=[WIDTH / 2, HEIGHT / 2], tag="snake"))


# Main game
def main():
    game_over = False
    reset()
    while True:
        if game_over:
            reset()
            game_over = False

        # Check for user input
        if

