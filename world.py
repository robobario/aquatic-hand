from arena import Arena

__author__ = 'python'


class WorldSnapshot:
    def __init__(self, arena):
        pass


class World:
    def __init__(self):
        self.pcs = []
        self.npcs = []
        self.arena = Arena(12, 12)

    def spawn(self, character):
        pass

    def attempt(self, who, action):
        self.pcaction(who, action)
        self.npcaction()
        return WorldSnapshot(self.arena)

    def pcaction(self, who, action):
        action.act(who, self)

    def npcaction(self):
        for npc in self.npcs:
            action = npc.decide(self.arena)
            action.act(npc, self.world)

    def move(self, who, direction):
        pass
