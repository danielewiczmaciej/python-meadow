from random import random, randrange

from direction import Direction
from grass import Grass


class Guarana(Grass):
    def __init__(self, _world=None, _x=None, _y=None, _age=0, _init=0, _power=0):
        super(Guarana, self).__init__(_world, _x, _y, _age, _init, _power)

    def GetSign(self):
        return '#'

    def Color(self):
        return "deep pink"

    def Divide(self, _chances):
        if len(_chances) == 0:
            return
        else:
            for i in range(randrange(len(_chances))):
                _chances.pop(0)
            if _chances[0] == Direction.UP:
                self.world.ToAdd(Guarana(self.world, self.x-1, self.y))
            elif _chances[0] == Direction.DOWN:
                self.world.ToAdd(Guarana(self.world, self.x+1, self.y))
            elif _chances[0] == Direction.RIGHT:
                self.world.ToAdd(Guarana(self.world, self.x, self.y + 1))
            elif _chances[0] == Direction.LEFT:
                self.world.ToAdd(Guarana(self.world, self.x, self.y - 1))

    def Collision(self, _collider):
        _collider.power += 3
        super().Collision(_collider)