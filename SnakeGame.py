from engine import *
from random import *

# Constant fields
WIDTH = 800
HEIGHT = 800
SPEED = 25
OBJECT_WIDTH = 25


# snake movement


def move_snake(code):
    if code == 37:
        snake.velocity = [-SPEED, 0]
    elif code == 39:
        snake.velocity = [SPEED, 0]
    elif code == 38:
        snake.velocity = [0, SPEED]
    elif code == 40:
        snake.velocity = [0, -SPEED]


def get_user_input(event):
    code = event.keycode
    move_snake(code)


window = WindowManager("Testing", 800, 800)
window.window.bind_all('<Key>', get_user_input)
canvas = window.get_canvas()
rectangle = canvas.create_rectangle(0, 0, 25, 25, fill="red")
canvas.pack()
window.show_window()


def reset():
    obj_list = {}
    snake = Snake()
    location_third = [WIDTH / 2 + 2 * OBJECT_WIDTH, HEIGHT/2]
    location_second = [WIDTH / 2 + OBJECT_WIDTH, HEIGHT / 2]
    location_first = [WIDTH / 2, HEIGHT / 2]
    third_body = GameObj(location=location_third, width=OBJECT_WIDTH, height=OBJECT_WIDTH, tag="snake")
    second_body = GameObj(location=location_second, width=OBJECT_WIDTH, height=OBJECT_WIDTH, tag="snake")
    first_body = GameObj(location=location_first, width=OBJECT_WIDTH, height=OBJECT_WIDTH, tag="snake")
    snake.insert(third_body)
    snake.insert(second_body)
    snake.insert(first_body)
    location_third = (WIDTH / 2 + 2 * OBJECT_WIDTH, HEIGHT / 2)
    location_second = (WIDTH / 2 + OBJECT_WIDTH, HEIGHT / 2)
    location_first = (WIDTH / 2, HEIGHT / 2)
    obj_list[location_third] = third_body
    obj_list[location_second] = second_body
    obj_list[location_first] = first_body


def movement():
    # remove snake tail
    remove_location = (snake.tail.game_obj.location[0], snake.tail.game_obj.location[1])
    obj_list.pop(remove_location)
    snake.remove()

    # add new body to the head
    head_location = snake.head.next.location

    # computer location
    location = [head_location[0] + snake.velocity[0], head_location[1] + snake.velocity[1]]

    # create snake body for head
    snake_body = GameObj(location=location, width=OBJECT_WIDTH, height=OBJECT_WIDTH, tag="snake")
    snake.insert(snake_body)
    location = (head_location[0] + snake.velocity[0], head_location[1] + snake.velocity[1])
    obj_list[location] = snake_body


# Generate food


def generate_food():
    random_x = random.randrange(0, WIDTH)
    random_y = random.randrange(0, HEIGHT)
    food = GameObj(location=[random_x, random_y], width=WIDTH, height=HEIGHT, tag="food")
    obj_list[(random_x, random_y)] = food


# snake body
snake = None
reset()

# create dictionary
obj_list = {}



# Main game
def main():
    game_over = False
    has_food = False
    while True:
        if game_over:
            reset()
            game_over = False

        # Check for user input

        movement()

        # Check if there is food, if not, then create one
        if not has_food:
            generate_food()
            has_food = True

        # Collision

