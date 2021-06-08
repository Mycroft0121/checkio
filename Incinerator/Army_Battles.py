class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        return self.health>0

class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7

def fight(u1, u2):
    while u1.health>0:
        u2.health -= u1.attack
        if not u2.is_alive:
            return True
        u1.health -= u2.attack
    return False


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, unit, num):
        for _ in range(num):
            self.units.append(unit())

    def unit_death(self):
        self.units.pop()

class Battle:
    def fight(self, att, deff):
        while len(att.units) > 0:
            if fight(att.units[-1], deff.units[-1]):
                deff.unit_death()
            else:
                att.unit_death()
            if not len(deff.units):
                return True
        return False
