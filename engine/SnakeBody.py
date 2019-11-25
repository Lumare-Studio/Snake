class SnakeBody(object):

    def __init__(self, game_obj=None):
        self.next = None
        self.prev = None
        self.game_obj = game_obj


class Snake(object):

    def __init__(self, velocity=[0, 0]):

        self.size = 0
        self.head = None
        self.tail = None
        self.velocity = velocity

    def insert(self, game_obj):
        new_body = SnakeBody(game_obj)
        if self.size == 0:
            self.head = new_body
            self.tail = new_body
        else:
            new_body = SnakeBody(game_obj)
            old_head = self.head
            old_head.prev = new_body
            self.head = new_body
            self.head.next = old_head

    def remove(self):
        if self.size > 0:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
