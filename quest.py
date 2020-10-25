from card import Card

class Quest(Card):
    def __init__(self, name, scenario, points):
        super(Quest, self).__init__(name)
        self.scenario = scenario
        self.points = points

    def copy(self):
        newQuest = Quest(self.name, self.scenario, self.points)
        return newQuest

    def getScenario(self):
        return self.scenario

    def getPoints(self):
        return self.points

    def setPoints(self, points):
        self.points = points

    def placeProgressTokens(self, progress):
        self.points -= progress
