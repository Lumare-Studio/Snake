from engine import *
from Snakelauncher import *

WIDTH = 800
HEIGHT = 800
OBJECT_WIDTH = 25

my_dict = DictManager(dict())
snake = Snake()
location_third = (WIDTH / 2 + 2 * OBJECT_WIDTH, HEIGHT / 2)
location_second = (WIDTH / 2 + OBJECT_WIDTH, HEIGHT / 2)
location_first = (WIDTH / 2, HEIGHT / 2)
third_body = GameObj(location=location_third, width=OBJECT_WIDTH, height=OBJECT_WIDTH, tag="snake")
second_body = GameObj(location=location_second, width=OBJECT_WIDTH, height=OBJECT_WIDTH, tag="snake")
first_body = GameObj(location=location_first, width=OBJECT_WIDTH, height=OBJECT_WIDTH, tag="snake")
snake.insert(third_body)
snake.insert(second_body)
snake.insert(first_body)

print(snake.tail.game_obj.tag, snake.tail.game_obj.location)
print(snake.tail.game_obj.tag, snake.head.game_obj.location)
print(snake.size)


# self.obj_list[location_third] = third_body
# my_dict(key=location_third, value=third_body)
# self.obj_list[location_second] = second_body
# my_dict(key=location_second, value=second_body)
# self.obj_list[location_first] = first_body
# my_dict(key=location_first, value=first_body)