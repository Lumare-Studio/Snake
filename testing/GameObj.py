class GameObj(object):
    x = 0
    y = 0

    #constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # return location
    def getLocation(self):
        print("x:", self.x, " y:", self.y)
