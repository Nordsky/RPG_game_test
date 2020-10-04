class Warrior():
    def __init__(self, lvl):
        self.name = "Воин"
        self.hp = lvl * 3
        self.df = lvl * 2
        self.mana = 0
        self.st = 2
        self.re = lvl
        self.vo = 1
        self.har = 0
        self.speed = -2
        #self.vnim = 0
        #self.sluh = 0
        #self.shadow = 0
        #self.noise = lvl
        self.gold = 3


class Wizard():
    def __init__(self, lvl):
        self.name = "Волшебник"
        self.hp = lvl
        self.df = lvl
        self.mana = lvl * 4
        self.st = 0
        self.re = lvl
        self.vo = lvl * 2
        self.har = 1
        self.speed = 1
        #self.vnim = lvl
        #self.sluh = lvl
        #self.shadow = -1
        #self.noise = 2
        self.gold = 13


class Archer():
    def __init__(self, lvl):
        self.name = "Лучник"
        self.hp = lvl * 1
        self.df = lvl * 1
        self.mana = lvl
        self.st = 1
        self.re = lvl * 2
        self.vo = 3
        self.har = 3
        self.speed = 2
        #self.vnim = 0
        #self.sluh = 0
        #self.shadow = 0
        #self.noise = lvl
        self.gold = 5