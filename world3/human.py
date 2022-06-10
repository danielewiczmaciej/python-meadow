from animal import Animal
from direction import Direction
from ground import Ground


class Human(Animal):

    turnsleft = 5

    def __init__(self, _world, _x, _y, _age=0, _init=5, _power=5, _turnsleft=5):
        self.world = _world
        self.x = _x
        self.y = _y
        self.age = _age
        self.initiative = _init
        self.power = _power
        self.turnsleft = _turnsleft

    def GetSign(self):
        return 'h'

    def Color(self):
        return "coral"

    def Action(self, dir=None):
        if self.CanMove(dir):
            if isinstance(self.Next(dir, 1), Ground):
                self.Move(dir)
            else:
                if self.Next(dir, 1).power < self.power:
                    if self.turnsleft > 0:
                        self.Immortality()
                self.Next(dir, 1).Collision(self)
                if isinstance(self.Next(dir, 1), Ground):
                    self.Move(dir)
        if self.turnsleft != 0:
            self.turnsleft -= 1

    def Immortality(self):
        self.world.Log("H is immortal!")
        chances = []
        if self.y == 0:
            if self.x == 0:
                if isinstance(self.world.board[self.y][self.x + 1], Ground):
                    chances.insert(len(chances), Direction.DOWN)
                if isinstance(self.world.board[self.y + 1][self.x], Ground):
                    chances.insert(len(chances), Direction.RIGHT)
            elif self.x == self.world.height - 1:
                if isinstance(self.world.board[self.y][self.x - 1], Ground):
                    chances.insert(len(chances), Direction.UP)
                if isinstance(self.world.board[self.y + 1][self.x], Ground):
                    chances.insert(len(chances), Direction.RIGHT)
            else:
                if isinstance(self.world.board[self.y][self.x - 1], Ground):
                    chances.insert(len(chances), Direction.UP)
                if isinstance(self.world.board[self.y][self.x + 1], Ground):
                    chances.insert(len(chances), Direction.DOWN)
                if isinstance(self.world.board[self.y + 1][self.x], Ground):
                    chances.insert(len(chances), Direction.RIGHT)
        elif self.y == self.world.width - 1:
            if self.x == 0:
                if isinstance(self.world.board[self.y][self.x + 1], Ground):
                    chances.insert(len(chances), Direction.DOWN)
                if isinstance(self.world.board[self.y - 1][self.x], Ground):
                    chances.insert(len(chances), Direction.LEFT)
            elif self.x == self.world.height - 1:
                if isinstance(self.world.board[self.y][self.x - 1], Ground):
                    chances.insert(len(chances), Direction.UP)
                if isinstance(self.world.board[self.y - 1][self.x], Ground):
                    chances.insert(len(chances), Direction.LEFT)
            else:
                if isinstance(self.world.board[self.y][self.x - 1], Ground):
                    chances.insert(len(chances), Direction.UP)
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
        if len(chances) == 0:
            return
        else:
            for i in range(len(chances)-1):
                chances.pop(0)
            if chances[0] == Direction.UP:
                self.Move(Direction.UP)
            if chances[0] == Direction.DOWN:
                self.Move(Direction.DOWN)
            if chances[0] == Direction.RIGHT:
                self.Move(Direction.RIGHT)
            if chances[0] == Direction.LEFT:
                self.Move(Direction.LEFT)

    def Collision(self, _collider):
        if self.turnsleft > 0:
            self.world.Log("h is immortal for the next" + str(self.turnsleft) + "turns")
            self.Immortality()
        else:
            if _collider.power > self.power:
                self.world.Log("h dies :( by " + _collider.GetSign())
                self.world.board[self.y][self.x] = Ground()
            else:
                self.world.Log("h overpowers " + _collider.GetSign())
                self.world.board[_collider.y][_collider.x] = Ground()

    def Print(self):
        out = self.GetSign() + ":" + str(self.x) + ":" + str(self.y) + ":" + str(self.age) + ":" + str(self.power) +\
              ":" + str(self.initiative) + ":" + str(self.turnsleft)
        return out

