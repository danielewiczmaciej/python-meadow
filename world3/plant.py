from organism import Organism
from ground import Ground


class Plant(Organism):
    def __init__(self, _world, _pos):
        super(_world, _pos)

    def Collision(self, _collider):
        if _collider.power > self.power:
            self.world.Log(_collider.GetSign() + " eats " + self.GetSign())
            self.world.board[self.y][self.x] = Ground()
        else:
            if _collider.GetSign() == "h" and self.world.sinceLastSuperAbility == 0:
                _collider.Immortality()
            else:
                self.world.Log(self.GetSign() + " kills " + _collider.GetSign())
                self.world.board[_collider.y][_collider.x] = Ground()
