from card import Card

class Land(Card):
    def __init__(self, name, threat, points):
        super(Land, self).__init__(name)
        self.threat = threat
        self.points = points

    def getThreat(self):
        return self.threat

    def getPoints(self):
        return self.points

    def setPoints(self, points):
        self.points = points

    def copy(self):
        newLand = Land(self.name, self.threat, self.points)
        return newLand

    def placeProgressTokens(self, progress):
        self.points -= progress
