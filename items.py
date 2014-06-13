__author__ = 'python'

available_powers = {"strength": 0,
                    "hp": 0}


class Item:
    def __eq__(self, other):
        return self.name == other.name \
               and self.description == other.description \
               and self.powers == other.powers \
               and self.types == other.types

    def __init__(self, name):
        self.name = name
        self.description = ""
        self.powers = available_powers
        self.types = []

    def __str__(self):
        return self.name

    def getdescription(self):
        return self.description


class ScimatarRune(Item):
    def __init__(self):
        super().__init__('scimatar rune')
        self.description = "A small stone depicting a vicious curved blade"
        self.types = ['fancy']
        self.powers["strength"] += 10


class MeatRune(Item):
    def __init__(self):
        super().__init__('meat rune')
        self.description = "A small stone depicting a lump of meat"
        self.types = ['fancy']
        self.powers["hp"] += 10


class Bone(Item):
    def __init__(self):
        super().__init__('bone')
        self.description = "A nondescript item"
        self.types = ['basic']