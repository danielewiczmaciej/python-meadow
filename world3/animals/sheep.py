from animal import Animal

class Sheep(Animal):
    def __init__(self, _world, _x, _y, _age=0, _init=4, _power=4):
        super(Sheep, self).__init__(_world, _x, _y, _age, _init, _power)

    def GetSign(self):
        return 's'

    def Color(self):
        return "white"

    def Split(self):
        self.Reproduce("sheep")