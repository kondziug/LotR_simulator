from deck import Deck
import globals

class QuestDeck(Deck):
    def __init__(self, name):
        super(QuestDeck, self).__init__(name)
        self.totalProgress = 0

    def copy(self):
        newQuestDeck = QuestDeck(self.name)
        newQuestDeck.cardList = self.cardList
        return newQuestDeck

    def getTotalProgress(self):
        return self.totalProgress

    def dealProgress(self, progress):
        if len(self.cardList) == 0:
            return
        self.totalProgress += progress
        card = self.cardList[0]
        card.placeProgressTokens(progress)
        if card.getPoints() <= 0:
            # self.takeOffTop()
            globals.gameWin = True
        
    def getCurrentQuest(self):
        return self.cardList[0]

    def setLastQuest(self, points):
        quest = self.cardList[-1]
        quest.setPoints(points)
