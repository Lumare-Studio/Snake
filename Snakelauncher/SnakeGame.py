from engine import *
import random
from engine.DictManager import *


class SnakeGame(object):

    def __init__(self):
        # snake body
        self.snake = None
        # create dictionary
        self.obj_manager = DictManager(origin_dict=dict())
        self.obj_list = self.obj_manager.copy_dict

        # create window
        self.window = WindowManager("Snake", 800, 800)
        self.window.window.bind_all('<Key>', self.get_user_input)

        # Constant fields
        self.WIDTH = 800
        self.HEIGHT = 800
        self.SPEED = 25
        self.OBJECT_WIDTH = 25
        self.has_food = False
        self.RANGE = int(self.WIDTH / self.OBJECT_WIDTH) - 1

    # add object to dictionary
    def add_obj(self, key, value):
        self.obj_manager.add(key=key, value=value)
        self.obj_list = self.obj_manager.copy_dict

    # delete object from dictionary
    def del_obj(self, key):
        self.obj_manager.remove(key=key)
        self.obj_list = self.obj_manager.copy_dict

    def clear(self):
        self.obj_manager.clear()
        self.obj_list = self.obj_manager.copy_dict

    # snake movement
    def move_snake(self, code):
        if code == 37:
            if self.snake.velocity[0] == 0:
                self.snake.velocity = [-self.SPEED, 0]
        elif code == 39:
            if self.snake.velocity[0] == 0:
                self.snake.velocity = [self.SPEED, 0]
        elif code == 38:
            if self.snake.velocity[1] == 0:
                self.snake.velocity = [0, -self.SPEED]
        elif code == 40:
            if self.snake.velocity[1] == 0:
                self.snake.velocity = [0, self.SPEED]

    def get_user_input(self, event):
        code = event.keycode
        self.move_snake(code)

    def reset(self):
        self.clear()
        self.snake = Snake()
        self.generate_food()
        location_third = (self.WIDTH / 2 + 2 * self.OBJECT_WIDTH, self.HEIGHT / 2)
        location_second = (self.WIDTH / 2 + self.OBJECT_WIDTH, self.HEIGHT / 2)
        location_first = (self.WIDTH / 2, self.HEIGHT / 2)
        third_body = GameObj(location=location_third, width=self.OBJECT_WIDTH, height=self.OBJECT_WIDTH, tag="snake")
        second_body = GameObj(location=location_second, width=self.OBJECT_WIDTH, height=self.OBJECT_WIDTH, tag="snake")
        first_body = GameObj(location=location_first, width=self.OBJECT_WIDTH, height=self.OBJECT_WIDTH, tag="snake")
        self.snake.insert(third_body)
        self.snake.insert(second_body)
        self.snake.insert(first_body)
        # self.obj_list[location_third] = third_body
        self.add_obj(key=location_third, value=third_body)
        # self.obj_list[location_second] = second_body
        self.add_obj(key=location_second, value=second_body)
        # self.obj_list[location_first] = first_body
        self.add_obj(key=location_first, value=first_body)

    def movement(self):
        # add new body to the head
        head_location = self.snake.head.game_obj.location

        # compute location
        location = (int(head_location[0] + self.snake.velocity[0]), int(head_location[1] + self.snake.velocity[1]))
        location = self.check_location(location)
        if location in self.obj_list.keys():
            temp_obj = self.obj_list[location]
            if isinstance(temp_obj, GameObj):
                if temp_obj.tag == "snake":
                    self.reset()
                else:
                    # create snake body for head
                    snake_body = GameObj(location=location, width=self.OBJECT_WIDTH, height=self.OBJECT_WIDTH,
                                         tag="snake")
                    self.snake.insert(snake_body)
                    # self.obj_list[location] = snake_body
                    self.add_obj(key=location, value=snake_body)
                    self.has_food = False
        else:
            # remove snake tail
            remove_location = (self.snake.tail.game_obj.location[0], self.snake.tail.game_obj.location[1])
            self.del_obj(remove_location)
            self.snake.remove()
            # create snake body for head
            snake_body = GameObj(location=location, width=self.OBJECT_WIDTH, height=self.OBJECT_WIDTH, tag="snake")
            self.snake.insert(snake_body)
            self.add_obj(key=location, value=snake_body)

    def check_location(self, location):
        new_location = None
        right_most_x = self.WIDTH - self.OBJECT_WIDTH
        bottom_most_y = self.HEIGHT - self.OBJECT_WIDTH
        if location[0] < 0:
            new_location = (right_most_x, location[1])
        elif location[0] > right_most_x:
            new_location = (0, location[1])
        elif location[1] < 0:
            new_location = (location[0], bottom_most_y)
        elif location[1] > bottom_most_y:
            new_location = (location[0], 0)
        else:
            new_location = location
        return new_location

    # Generate food

    def generate_food(self):
        RANGE = self.RANGE
        random_x = random.randint(0, RANGE) * self.OBJECT_WIDTH
        random_y = random.randint(0, RANGE) * self.OBJECT_WIDTH
        location = (random_x, random_y)
        while location in self.obj_list.keys():
            RANGE = self.RANGE
            random_x = random.randint(0, RANGE) * self.OBJECT_WIDTH
            random_y = random.randint(0, RANGE) * self.OBJECT_WIDTH
            location = (random_x, random_y)
        food = GameObj(location=location, width=self.OBJECT_WIDTH, height=self.OBJECT_WIDTH, tag="food",
                       color="green")
        self.add_obj(key=(random_x, random_y), value=food)

    # Main game
    def main(self):
        self.reset()
        game_over = False
        self.has_food = True
        while True:
            if game_over:
                self.reset()
                game_over = False

            # Check for user input

            self.movement()

            # Check if there is food, if not, then create one
            if not self.has_food:
                self.generate_food()
                self.has_food = True
            time.sleep(0.05)
