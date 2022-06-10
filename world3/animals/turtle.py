from animal import Animal
from random import random, randrange
from ground import Ground


class Turtle(Animal):
    def __init__(self, _world, _x, _y, _age=0, _init=1, _power=2):
        super(Turtle, self).__init__(_world, _x, _y, _age, _init, _power)

    def GetSign(self):
        return 't'

    def Color(self):
        return "green"

    def Split(self):
        self.Reproduce("turtle")

    def Action(self):
        rand = randrange(4)
        if rand == 0:
            dir = self.NewDir()
            if self.CanMove(dir):
                if isinstance(self.Next(dir, 1), Ground):
                    self.Move(dir)
                else:
                    self.Next(dir, 1).Collision(self)
                    if isinstance(self.Next(dir, 1), Ground):
                        self.Move(dir)

    def Collision(self, _collider):
        if _collider.GetSign() == self.GetSign():
            self.Split()
        elif _collider.power < 5:
            self.world.Log(_collider.GetSign() + " stops " + self.GetSign())
        elif _collider.power > self.power:
            self.world.Log(_collider.GetSign() + " kills " + self.GetSign())
            self.world.board[self.y][self.x] = Ground()
        else:
            self.world.Log(self.GetSign() + " kills " + _collider.GetSign())
            self.world.board[_collider.y][_collider.x] = Ground()