class ObjManager(object):

    def __init__(self, width = 0, height = 0):
        self.ObjList = [None]
        self.ObjGrid = [[None]*width]*height

    def addObj(self, Obj = None):
        if Obj != None:
            self.objList.append(Obj)
