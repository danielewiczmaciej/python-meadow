import math

from animal import Animal
from direction import Direction
from ground import Ground
from plants.Borscht import Borscht


class CyberSheep(Animal):
    def __init__(self, _world=None, _x=None, _y=None, _age=0, _init=4, _power=11):
        super(CyberSheep, self).__init__(_world, _x, _y, _age, _init, _power)

    def GetSign(self):
        return 'c'

    def Color(self):
        return "cyan"

    def Split(self):
        self.Reproduce("cybersheep")

    def Action(self, dir=None):
        dir = self.FindClosestB()
        if self.CanMove(dir):
            if isinstance(super().Next(dir, 1), Ground):
                super().Move(dir)
            else:
                super().Next(dir, 1).Collision(self)
                if isinstance(super().Next(dir, 1), Ground):
                    super().Move(dir)

    def FindClosestB(self):
        distance = math.sqrt(math.pow(self.world.height, 2) + math.pow(self.world.width, 2))
        temp = None
        Bexist = False
        X=0
        Y=0
        dir = None
        for it in self.world.organisms:
            if isinstance(it, Borscht) and isinstance(self.world.board[it.y][it.x], Borscht):
                print("found")
                Bexist = True
                break
        if Bexist:
            for it in self.world.organisms:
                if isinstance(it, Borscht) and isinstance(self.world.board[it.y][it.x], Borscht):
                    temp = math.sqrt(math.pow(it.x - self.x, 2) + math.pow(it.y-self.y, 2))
                    if temp < distance:
                        distance = temp
                        self.X = it.x
                        self.Y = it.y
            print("CS location: (", str(self.x) + ", " + str(self.y) + ")")
            print("B location: (", str(self.X) + ", " + str(self.Y) + ")")
            if abs(self.x - self.X) > abs(self.y - self.Y):
                if self.x > self.X:
                    dir = Direction.UP
                else:
                    dir = Direction.DOWN
            else:
                if self.y > self.Y:
                    dir = Direction.LEFT
                else:
                    dir = Direction.RIGHT
            print(str(dir) + "(" + str(self.x) + ", " + str(self.y) + ")")
            return dir
        else:
            return super().NewDir()