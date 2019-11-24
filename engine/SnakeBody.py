class SnakeBody(object):

    def __init__(self, game_obj):
        self.next = None
        self.prev = None
        self.game_obj = game_obj


class Snake(object):

    def __init__(self, velocity=[-25, 0]):
        self.head = SnakeBody()
        self.tail = self.head
        self.velocity = velocity

        self.size = 0

    def insert(self, game_obj):
        snake_body = SnakeBody(game_obj)
        temp = self.head.next
        self.head.next = snake_body
        temp.prev = self.head.next
        self.head.next.next = temp
        if self.size == 0:
            self.tail = self.tail.next
        self.size += 1

    def remove(self):
        temp = None
        if self.size > 0:
            temp = self.tail.prev
            self.tail.prev = None
            self.tail = temp
            self.tail.next = None
            self.size -= 1
        return temp
