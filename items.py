__author__ = 'python'

class Item:
    def __init__(self, name = "Chicken bone"):
        self.name = name
        self.description = "A nondescript item"
        self.power = []
        self.type = []

    def __str__(self):
        return self.name

    def getdescription(self):
        return self.description

class ScimatarRune(Item):
    def __init__(self):
        super().__init__('Scimatar Rune')
        self.description = "A small stone depicting a vicious curved blade"