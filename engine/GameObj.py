class GameObj(object):
    loc = None #location
    vel = None #velocity
    acc = None #acceleration

    def __init__(self, location = [0, 0], velocity = [0, 0], acceleration =[0, 0]):
        self.loc = location
        self.vel = velocity
        self.acc = acceleration



