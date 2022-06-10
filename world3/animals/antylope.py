from random import random, randrange

from animal import Animal
from direction import Direction
from ground import Ground


class Antylope(Animal):
    def __init__(self, _world, _x, _y, _age=0, _init=4, _power=4):
        super(Antylope, self).__init__(_world, _x, _y, _age, _init, _power)

    def GetSign(self):
        return 'a'

    def Color(self):
        return "khaki2"

    def Split(self):
        self.Reproduce("antylope")

    def Action(self):
        dir = super().NewDir()
        if (dir == Direction.UP and self.x > 1 or
                dir == Direction.DOWN and self.x < self.world.height - 2 or
                dir == Direction.RIGHT and self.y < self.world.width - 2 or
                dir == Direction.LEFT and self.y > 1):
            if isinstance(super().Next(dir, 1), Ground):
                if isinstance(super().Next(dir, 2), Ground):
                    super().Move(dir)
                    super().Move(dir)
                else:
                    super().Move(dir)
                    super().Next(dir, 1).Collision(self)
                    if isinstance(super().Next(dir, 1), Ground):
                        super().Move(dir)
            else:
                super().Next(dir, 1).Collision(self)
                if isinstance(super().Next(dir, 1), Ground):
                    super().Move(dir)

    def NewDir(self):
        dir = None
        if self.y == 0 or self.y == 1:
            if self.x == 0:
                temp = randrange(2)
                if temp == 0:
                    dir = Direction.DOWN
                else:
                    dir = Direction.RIGHT

            elif self.x == self.world.height - 1:
                temp = randrange(2)
                if temp == 0:
                    dir = Direction.UP
                else:
                    dir = Direction.RIGHT
            else:
                temp = randrange(3)

                if temp == 0:
                    dir = Direction.UP
                if temp == 1:
                    dir = Direction.DOWN
                if temp == 2:
                    dir = Direction.RIGHT

        elif self.y == self.world.width - 1 or self.y == self.world.width -2:  # top right
            if self.x == 0:
                temp = randrange(2)
                if temp == 0:
                    dir = Direction.DOWN
                else:
                    dir = Direction.LEFT

            elif self.x == self.world.height - 1:
                temp =randrange(2)
                if temp == 0:
                    dir = Direction.UP
                else:
                    dir = Direction.LEFT

            else:
                temp = randrange(3)

                if temp == 0: dir = Direction.UP
                if temp == 1: dir = Direction.DOWN
                if temp == 2: dir = Direction.LEFT

        elif self.x == 0 or self.x == 1:
            temp = randrange(3)

            if temp == 0: dir = Direction.RIGHT
            if temp == 1: dir = Direction.DOWN
            if temp == 2: dir = Direction.LEFT

        elif self.x == self.world.height - 1 or self.x == self.world.height -2:
            temp = randrange(2)
            if temp == 0: dir = Direction.UP
            if temp == 1: dir = Direction.RIGHT
            if temp == 2: dir = Direction.LEFT

        else:
            temp = randrange(4)
            if temp == 0:
                dir = Direction.UP
            if temp == 1:
                dir = Direction.DOWN
            if temp == 2:
                dir = Direction.LEFT
            if temp == 4:
                dir = Direction.RIGHT

        return dir

    def Collision(self, _collider):
        temp = randrange(2)
        if isinstance(_collider, Antylope):
            self.Split()
        elif temp == 0:
            self.world.Log("a tries to run away!")
            if self.y > 0 and isinstance(super().Next(Direction.LEFT, 1), Ground):
                super().Move(Direction.LEFT)
            elif self.y < self.world.width - 1 and isinstance(super().Next(Direction.RIGHT, 1), Ground):
                super().Move(Direction.RIGHT)
            elif self.x > 0 and isinstance(super().Next(Direction.UP, 1), Ground):
                super().Move(Direction.UP)
            elif self.x < self.world.height-1 and isinstance(super().Next(Direction.DOWN, 1), Ground):
                super().Move(Direction.DOWN)
        elif _collider.power > self.power:
            self.world.Log(_collider.GetSign() + " kills " + self.GetSign())
            self.world.board[self.y][self.x] = Ground()
        else:
            self.world.Log(self.GetSign() + " kills " + _collider.GetSign())
            self.world.board[_collider.y][_collider.x] = Ground()