# Taken from mission The Defenders

# Taken from mission Army Battles

class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5


    @property
    def is_alive(self):
        return self.health>0

    def attack_enermy(self, enermy):
        return enermy.take_attack(self.attack)

    def take_attack(self,att):
        self.health -= att
        return att

class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7

class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 3
        self.defense = 2

    def take_attack(self, att):
        self.health -= max(0, att-self.defense)
        return max(0, att-self.defense)

class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.attack = 4
        self.vampirism = 50

    def attack_enermy(self, enermy):
        dmg = super(Vampire,self).attack_enermy(enermy)
        self.health+=dmg*self.vampirism/100
        return dmg
