class ObjManager(object):

    def __init__(self, width=0, height=0):
        self.obj_list = [None]
        self.obj_grid = [[None]*width]*height

    def add_obj(self, obj=None):
        if obj != None:
            self.objList.append(obj)
