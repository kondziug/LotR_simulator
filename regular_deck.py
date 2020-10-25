import random
from deck import Deck

class RegularDeck(Deck):
    def __init__(self, name):
        super(RegularDeck, self).__init__(name)

    def copy(self):
        newRegularDeck = RegularDeck(self.name)
        newRegularDeck.cardList = self.cardList
        return newRegularDeck

    def shuffle(self):
#        random.seed(1)
        random.shuffle(self.cardList)
    

        