class Deck:
    def __init__(self, name):
        self.name = name
        self.cardList = []

    def getName(self):
        return self.name

    def getCardList(self):
        return self.cardList

    def takeOffTop(self):
        return self.pullCard(0)

    def pullCard(self, index):
        if not self.cardList:
            return
        card = self.cardList[index]
        self.cardList = self.cardList[:index] + self.cardList[(index+1):]
        return card

    def size(self):
        return len(self.cardList)

    def addCard(self, card, number):
        for i in range(0, number):
            tempCard = card.copy()
            self.cardList.append(tempCard)

    def removeCard(self, card):
        self.cardList.remove(card)

    def findCopyOfCard(self, name):
        for card in self.cardList:
            if card.getName() == name:
                return card

    def getAllNames(self):
        names = [self.cardList[0].getName()]
        i = 1
        while i < len(self.cardList):
            name = self.cardList[i].getName()
            i += 1
            if names.count(name) > 0:
                continue
            names.append(name)
        return names



    
