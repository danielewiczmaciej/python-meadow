from random import random, randrange
from direction import Direction


class Organism:
    age = 0
    power = 0
    initiative = 0
    world = None
    x = None
    y = None

    def __init__(self, _world=None, _x=None, _y=None, _age=0, _init=None, _power=None):
        self.world = _world
        self.x = _x
        self.y = _y
        self.age = _age
        self.initiative = _init
        self.power = _power

    def Action(self, _dir=None):
        pass

    def Collision(self, _collider):
        if _collider.power > self.power:
            self.world.Log(_collider.GetSign() + " kills " + self.GetSign())
            from ground import Ground
            self.world.board[self.y][self.x] = Ground()
        else:
            pass

    def Color(self):
        pass

    def GetSign(self):
        pass

    def RandDir(self):
        rand = randrange(4)
        if rand == 0:
            return Direction.UP
        elif rand == 1:
            return Direction.DOWN
        elif rand == 2:
            return Direction.LEFT
        elif rand == 3:
            return Direction.RIGHT
        else:
            pass

    def Next(self, _dir, _dist):
        if _dir == Direction.UP:
            if self.x - _dist >= 0:
                return self.world.board[self.y][self.x - _dist]
            else:
                return None
        elif _dir == Direction.DOWN:
            if self.x + _dist < self.world.width:
                return self.world.board[self.y][self.x + _dist]
            else:
                return None
        elif _dir == Direction.LEFT:
            if self.y - _dist >= 0:
                return self.world.board[self.y - _dist][self.x]
            else:
                return None
        elif _dir == Direction.RIGHT:
            if self.y + _dist < self.world.height:
                return self.world.board[self.y + _dist][self.x]
            else:
                return None
        else:
            pass

    def Print(self):
        out = self.GetSign() + ":" + str(self.x) + ":" + str(self.y) + ":" + str(self.age) + ":" + str(self.power) +\
              ":" + str(self.initiative)
        return out

