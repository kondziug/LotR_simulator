from creature import Creature

class Enemy(Creature):
    def __init__(self, name, attack, defense, hitpoints, engagement, threat):
        super(Enemy, self).__init__(name, attack, defense, hitpoints)
        self.engagement = engagement
        self.threat = threat

    def getEngagement(self):
        return self.engagement

    def getThreat(self):
        return self.threat

    def copy(self):
        newEnemy = Enemy(self.name, self.attack, self.defense, self.hitpoints, self.engagement, self.threat)
        return newEnemy
