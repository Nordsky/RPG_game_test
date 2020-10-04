class Human():
    def __init__(self, lvl):
        self.name = "Человек"
        self.hp = lvl*5
        self.df = lvl
        self.mana = lvl*2
        self.st = 1
        self.re = lvl
        self.vo = 0
        self.har = lvl*2
        self.speed = 5
        #self.vnim = lvl
        #self.sluh = lvl
        #self.shadow = lvl
        #self.noise = lvl+1
        self.gold = 9


class WoodElf():
    def __init__(self, lvl):
        self.name = "Лесной эльф"
        self.hp = 3*lvl
        self.df = lvl
        self.mana = lvl*3
        self.st = 1
        self.re = lvl*2
        self.vo = 2
        self.har = lvl
        self.speed = 8
        #self.vnim = lvl+2
        #self.sluh = lvl+1
        #self.shadow = lvl*2
        #self.noise = 1
        self.gold = 4


class Orc():
    def __init__(self, lvl):
        self.name = "Орк"
        self.hp = 7*lvl
        self.df = 2*lvl
        self.mana = lvl*1
        self.st = 4
        self.re = lvl
        self.vo = 0
        self.har = 1
        self.speed = 7
        #self.vnim = lvl
        #self.sluh = lvl*3
        #self.shadow = lvl*1
        #self.noise = 0
        self.gold = 1


class Dworf():
    def __init__(self, lvl):
        self.name = "Дворф"
        self.hp = lvl*3
        self.df = lvl*3
        self.mana = lvl*1
        self.st = lvl*2
        self.re = 0
        self.vo = lvl
        self.har = -2
        self.speed = 3
        #self.vnim = lvl
        #self.sluh = lvl
        #self.shadow = lvl
        #self.noise = lvl+1
        self.gold = 25