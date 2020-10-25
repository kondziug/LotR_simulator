from land import Land
from enemy import Enemy

class Board:
    def __init__(self, questDeck, encounterDeck, stagingArea, engagementArea, activeLand):
        self.questDeck = questDeck
        self.encounterDeck = encounterDeck
        self.stagingArea = stagingArea
        self.engagementArea = engagementArea
        self.activeLand = activeLand
        self.combinedThreat = 0
        self.setCombinedThreat()
        self.shuffleEncounterDeck()

    # watch out!!!!!!!!!!!!
    def copy(self):
        newBoard = Board(self.questDeck, self.encounterDeck, self.stagingArea, self.engagementArea, self.activeLand)
        return newBoard

    def getQuestDeck(self):
        return self.questDeck

    def getEncounterDeck(self):
        return self.encounterDeck

    def getStagingArea(self):
        return self.stagingArea

    def getEnemiesEngaged(self):
        return self.engagementArea

    def getAllLands(self):
        lands = []
        for card in self.stagingArea:
            if isinstance(card, Land):
                lands.append(card)
        return lands

    def getAllEnemies(self):
        enemies = []
        for card in self.stagingArea:
            if isinstance(card, Enemy):
                enemies.append(card)
        return enemies

    def getActiveLand(self):
        if self.activeLand:
            return self.activeLand[0]
        else:
            return None

    def getCombinedThreat(self):
        return self.combinedThreat

    def setCombinedThreat(self):
        if not self.stagingArea:
            return
        for card in self.stagingArea:
            self.combinedThreat += card.getThreat()

    def shuffleEncounterDeck(self):
        self.encounterDeck.shuffle()

    def revealCard(self):
        return self.encounterDeck.takeOffTop()

    def addCard(self, card):
        self.stagingArea.append(card)
        self.combinedThreat += card.getThreat()

    def scenarioSetup(self):
        forestSpider = self.encounterDeck.findCopyOfCard('Forest Spider')
        oldForestRoad = self.encounterDeck.findCopyOfCard('Old Forest Road')
        self.addCard(forestSpider)
        self.addCard(oldForestRoad)
        self.encounterDeck.removeCard(forestSpider)
        self.encounterDeck.removeCard(oldForestRoad)
        self.shuffleEncounterDeck()

    def addToStagingArea(self):
        card = self.revealCard()
        if not card:
            return
        self.addCard(card)

    def removeFromStagingArea(self, card):
        self.combinedThreat -= card.getThreat()
        self.stagingArea.remove(card)

    def dealProgress(self, progress):
        if self.activeLand:
            self.activeLand[0].placeProgressTokens(progress)
            if self.activeLand[0].getPoints() <= 0:
                self.activeLand = []
        else:
            self.questDeck.dealProgress(progress)
        
    def travelToLocation(self, card):
        self.removeFromStagingArea(card)
        self.activeLand.append(card)

    def doEngagementChecks(self, threat):
        enemies = self.getAllEnemies()
        for enemy in enemies:
            if enemy.engagement <= threat:
                self.addToEngagementArea(enemy)

    def addToEngagementArea(self, card):
        self.removeFromStagingArea(card)
        self.engagementArea.append(card)

    def removeFromEngagementArea(self, card):
        self.engagementArea.remove(card)

    def clearDeads(self):
        for enemy in self.engagementArea:
            if enemy.isDead():
                self.removeFromEngagementArea(enemy)

    def endTurn(self):
        self.clearDeads()
