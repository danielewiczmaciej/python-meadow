from random import random, randrange

from animal import Animal
from direction import Direction
from grass import Grass
from ground import Ground
from human import Human


class Borscht(Grass):
    def __init__(self, _world=None, _x=None, _y=None, _age=0, _init=0, _power=10):
        super(Borscht, self).__init__(_world, _x, _y, _age, _init, _power)

    def GetSign(self):
        return '$'

    def Color(self):
        return "red4"

    def Divide(self, _chances):
        if len(_chances) == 0:
            return
        else:
            for i in range(randrange(len(_chances))):
                _chances.pop(0)
            if _chances[0] == Direction.UP:
                self.world.ToAdd(Borscht(self.world, self.x - 1, self.y))
            elif _chances[0] == Direction.DOWN:
                self.world.ToAdd(Borscht(self.world, self.x + 1, self.y))
            elif _chances[0] == Direction.RIGHT:
                self.world.ToAdd(Borscht(self.world, self.x, self.y + 1))
            elif _chances[0] == Direction.LEFT:
                self.world.ToAdd(Borscht(self.world, self.x, self.y - 1))

    def Collision(self, _collider):
        from animals.cybersheep import CyberSheep
        if not isinstance(_collider, CyberSheep):
            self.world.Log(self.GetSign() + " burns " + _collider.GetSign())
            self.world.board[self.y][self.x] = Ground()
            self.world.board[_collider.y][_collider.x] = Ground()
        else:
            self.world.Log(_collider.GetSign() + " eats " + self.GetSign())
            self.world.board[self.y][self.x] = Ground()

    def Check(self, x, y):
        from animals.cybersheep import CyberSheep
        if self.x + x > 0 and self.x + x < self.world.height - 1 and self.y + y < self.world.width - 1 and self.y + y > 0:
            if isinstance(self.world.board[self.y + y][self.x + x], Animal) and not \
                    isinstance(self.world.board[self.y + y][self.x + x], CyberSheep):
                if isinstance(self.world.board[self.y + y][self.x + x], Human) and self.world.sinceLastSuperAbility == 0:
                    self.world.board[self.y + y][self.x + x].Immortality()
                else:
                    self.world.board[self.y + y][self.x + x] = Ground()

    def Burn(self):
        if self.y == 0:
            if self.x == 0:
                self.Check(0, 1)
                self.Check(1, 1)
                self.Check(1, 0)
            elif self.x == self.world.height - 1:
                self.Check(0, -1)
                self.Check(1, -1)
                self.Check(1, 0)
            else:
                self.Check(0, -1)
                self.Check(1, -1)
                self.Check(1, 0)
                self.Check(0, 1)
                self.Check(1, 1)
        elif self.y == self.world.width - 1:
            if self.x == 0:
                self.Check(0, 1)
                self.Check(-1, 1)
                self.Check(-1, 0)
            elif self.x == self.world.height - 1:
                self.Check(0, -1)
                self.Check(-1, -1)
                self.Check(-1, 0)
            else:
                self.Check(0, -1)
                self.Check(-1, -1)
                self.Check(-1, 0)
                self.Check(0, 1)
                self.Check(-1, 1)
        elif self.x == 0:
            self.Check(0, 1)
            self.Check(1, 1)
            self.Check(-1, 1)
            self.Check(1, 0)
            self.Check(-1, 0)
        elif self.x == self.world.height - 1:
            self.Check(0, -1)
            self.Check(1, -1)
            self.Check(-1, -1)
            self.Check(1, 0)
            self.Check(-1, 0)

        else:
            self.Check(0, -1)
            self.Check(1, -1)
            self.Check(-1, -1)
            self.Check(1, 0)
            self.Check(-1, 0)
            self.Check(0, 1)
            self.Check(1, 1)
            self.Check(-1, 1)