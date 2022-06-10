from organism import Organism


class Ground(Organism):

    def __init__(self, _world=None, _x=None, _y=None, _age=0, _init=0, _power=0):
        super(Ground, self).__init__(_world, _x, _y, _age, _init, _power)

    def Color(self):
        return "sandy brown"

    def GetSign(self):
        return '_'