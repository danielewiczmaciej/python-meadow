from animal import Animal


class Wolf(Animal):
    def __init__(self, _world, _x, _y, _age=0, _init=5, _power=9):
        super(Wolf, self).__init__(_world, _x, _y, _age, _init, _power)

    def GetSign(self):
        return 'w'

    def Color(self):
        return "black"

    def Split(self):
        self.Reproduce("wolf")