class SnakeBody(object):

    def __int__(self, game_obj=None):
        self.next = None
        self.prev = None
        self.GameObj = game_obj


class Snake(object):

    def __int__(self):
        self.head = SnakeBody()
        self.tail = self.head

        self.size = 0

    def insert(self, snake_body):
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
