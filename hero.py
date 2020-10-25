from player_creature import PlayerCreature

class Hero(PlayerCreature):
    def __init__(self, name, attack, defense, hitpoints, willpower, sphere, threat):
        super(Hero, self).__init__(name, attack, defense, hitpoints, willpower, sphere)
        self.threat = threat
        self.resourcePool = 0

    def getThreat(self):
        return self.threat

    def getResourcePool(self):
        return self.resourcePool

    def setResourcePool(self, resourcePool):
        self.resourcePool = resourcePool

    def copy(self):
        newHero = Hero(self.name, self.attack, self.defense, self.hitpoints, self.willpower, self.sphere, self.threat)
        newHero.resourcePool = self.resourcePool
        return newHero

    def addResourceToken(self):
        self.resourcePool += 1

    def spendResourceTokens(self, cost):
        tokensLeft = 0
        self.resourcePool -= cost
        if self.resourcePool < 0:
            tokensLeft = -self.resourcePool
            self.resourcePool = 0
        return tokensLeft
