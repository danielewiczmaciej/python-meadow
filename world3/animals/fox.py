from animal import Animal
from ground import Ground


class Fox(Animal):
    def __init__(self, _world, _x, _y, _age=0, _init=7, _power=3):
        super(Fox, self).__init__(_world, _x, _y, _age, _init, _power)

    def GetSign(self):
        return 'f'

    def Color(self):
        return "orange red"

    def Split(self):
        self.Reproduce("fox")

    def Action(self):
        dir = super().RandDir()
        if self.CanMove(dir):
            if isinstance(super().Next(dir, 1), Ground):
                super().Move(dir)
            else:
                if super().Next(dir, 1) is not None:
                    if super().Next(dir, 1).power < self.power:
                        super().Next(dir, 1).Collision(self)
                        if isinstance(super().Next(dir, 1), Ground):
                            super().Move(dir)