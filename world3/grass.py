from random import random, randrange
from direction import Direction
from ground import Ground
from organism import Organism


class Grass(Organism):
    def __init__(self,  _world=None, _x=None, _y=None, _age=0, _init=0, _power=0):
        super(Grass, self).__init__(_world, _x, _y, _age, _init, _power)

    def GetSign(self):
        return '.'

    def Color(self):
        return "green2"

    def Action(self, _dir=None):
        temp = randrange(10)
        chances = []
        if temp == 0:
            if self.y == 0:
                if self.x == 0:
                    if isinstance(self.world.board[self.y][self.x + 1], Ground):
                        chances.insert(len(chances), Direction.DOWN)
                    if isinstance(self.world.board[self.y+1][self.x], Ground):
                        chances.insert(len(chances), Direction.RIGHT)
                elif self.x == self.world.height - 1:
                    if isinstance(self.world.board[self.y][self.x - 1], Ground):
                        chances.insert(len(chances), Direction.UP)
                    if isinstance(self.world.board[self.y + 1][self.x], Ground):
                        chances.insert(len(chances), Direction.RIGHT)
                else:
                    if isinstance(self.world.board[self.y][self.x - 1], Ground):
                        chances.insert(len(chances),Direction.UP)
                    if isinstance(self.world.board[self.y][self.x + 1], Ground):
                        chances.insert(len(chances), Direction.DOWN)
                    if isinstance(self.world.board[self.y + 1][self.x], Ground):
                        chances.insert(len(chances), Direction.RIGHT)
            elif self.y == self.world.width - 1:
                if self.x == 0:
                    if isinstance(self.world.board[self.y][self.x + 1], Ground):
                        chances.insert(len(chances), Direction.DOWN)
                    if isinstance(self.world.board[self.y-1][self.x], Ground):
                        chances.insert(len(chances), Direction.LEFT)
                elif self.x == self.world.height - 1:
                    if isinstance(self.world.board[self.y][self.x - 1], Ground):
                        chances.insert(len(chances), Direction.UP)
                    if isinstance(self.world.board[self.y - 1][self.x], Ground):
                        chances.insert(len(chances), Direction.LEFT)
                else:
                    if isinstance(self.world.board[self.y][self.x - 1], Ground):
                        chances.insert(len(chances),Direction.UP)
                    if isinstance(self.world.board[self.y][self.x + 1], Ground):
                        chances.insert(len(chances), Direction.DOWN)
                    if isinstance(self.world.board[self.y - 1][self.x], Ground):
                        chances.insert(len(chances), Direction.LEFT)
            elif self.x == 0:
                if isinstance(self.world.board[self.y][self.x + 1], Ground):
                    chances.insert(len(chances), Direction.DOWN)
                if isinstance(self.world.board[self.y - 1][self.x], Ground):
                    chances.insert(len(chances), Direction.LEFT)
                if isinstance(self.world.board[self.y + 1][self.x], Ground):
                    chances.insert(len(chances), Direction.RIGHT)
            elif self.x == self.world.height - 1:
                if isinstance(self.world.board[self.y][self.x - 1], Ground):
                    chances.insert(len(chances), Direction.UP)
                if isinstance(self.world.board[self.y - 1][self.x], Ground):
                    chances.insert(len(chances), Direction.LEFT)
                if isinstance(self.world.board[self.y + 1][self.x], Ground):
                    chances.insert(len(chances), Direction.RIGHT)
            else:
                if isinstance(self.world.board[self.y][self.x + 1], Ground):
                    chances.insert(len(chances), Direction.DOWN)
                if isinstance(self.world.board[self.y - 1][self.x], Ground):
                    chances.insert(len(chances), Direction.LEFT)
                if isinstance(self.world.board[self.y + 1][self.x], Ground):
                    chances.insert(len(chances), Direction.RIGHT)
                if isinstance(self.world.board[self.y][self.x - 1], Ground):
                    chances.insert(len(chances), Direction.UP)
        self.Divide(chances)

    def Divide(self, _chances):
        if len(_chances) == 0:
            return
        else:
            for i in range(randrange(len(_chances))):
                _chances.pop(0)
            if _chances[0] == Direction.UP:
                self.world.ToAdd(Grass(self.world, self.x-1, self.y))
            elif _chances[0] == Direction.DOWN:
                self.world.ToAdd(Grass(self.world, self.x+1, self.y))
            elif _chances[0] == Direction.RIGHT:
                self.world.ToAdd(Grass(self.world, self.x, self.y + 1))
            elif _chances[0] == Direction.LEFT:
                self.world.ToAdd(Grass(self.world, self.x, self.y - 1))

    def Collision(self, _collider):
        self.world.Log(_collider.GetSign() + " eats " + self.GetSign())
        self.world.board[self.y][self.x] = Ground()
