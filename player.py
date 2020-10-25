import random
import globals

class Player:
    def __init__(self, playerDeck, heroes, hand, allies, threat):
        self.playerDeck = playerDeck
        self.heroes = heroes
        self.hand = hand
        self.allies = allies
        self.threat = threat
        self.shufflePlayerDeck()

    def copy(self):
        newPlayer = Player(self.playerDeck, self.heroes, self.hand, self.allies, self.threat)
        return newPlayer

    def getPlayerDeck(self):
        return self.playerDeck

    def getHand(self):
        return self.hand

    def findCardInHand(self, name):
        for card in self.hand:
            if card.getName() == name:
                return card
        return None

    def findCardInPlay(self, name):
        for card in self.getAllCharacters():
            if card.getName() == name:
                return card
        return None

    def getHeroes(self):
        return self.heroes

    def getAllies(self):
        return self.allies

    def getAllCharacters(self):
        return self.heroes + self.allies

    def getCharactersBySphere(self, sphere):
        characters = self.getAllCharacters()
        bySphere = []
        for character in characters:
            if character.getSphere() == sphere:
                bySphere.append(character)
        return bySphere

    def getUntappedCharacters(self):
        characters = self.getAllCharacters()
        untappedCharacters = []
        for character in characters:
            if not character.isTapped():
                untappedCharacters.append(character)
        return untappedCharacters

    def getThreat(self):
        return self.threat

    def draw(self):
        if self.playerDeck.size() > 0:
            self.hand.append(self.playerDeck.takeOffTop())

    def readyTurn(self):
        for hero in self.heroes:
            hero.addResourceToken()
        self.draw()

    def shufflePlayerDeck(self):
        self.playerDeck.shuffle()

    def drawHand(self):
        for i in range(0, 7):
            self.draw()

    def getResourcesBySphere(self, sphere):
        total = 0
        for hero in self.heroes:
            if hero.sphere == sphere or sphere == 'Neutral':
                total += hero.getResourcePool()
        return total

    def spendResourcesBySphere(self, sphere, cost):
        tokensLeft = cost
        for hero in self.heroes:
            if tokensLeft and hero.sphere == sphere or sphere == 'Neutral':
                tokensLeft = hero.spendResourceTokens(tokensLeft)

    def addToAllies(self, card):
        self.hand.remove(card)
        self.allies.append(card)

    def increaseThreat(self, threat):
        self.threat += threat
        if self.threat >= 50 or not self.heroes:
            globals.gameOver = True
            return

    def checkIfAllTapped(self):
        characters = self.getAllCharacters()
        for character in characters:
            if not character.isTapped():
                return False
        return True

    def untapAll(self):
        for hero in self.heroes:
            hero.untap()
        for ally in self.allies:
            ally.untap()

    def declareRandomDefender(self):
        untappedCharacters = self.getUntappedCharacters()
        if untappedCharacters and random.random() < 0.5:
            defender = random.choice(untappedCharacters)
            defender.tap()
            return defender
        else:
            return None

    def randomUndefended(self, attack):
        if self.heroes:
            randomHero = random.choice(self.heroes)
            randomHero.takeDamage(attack)
            if randomHero.isDead():
                self.heroes.remove(randomHero)
        else:
            globals.gameOver = True

    def findAndSpend(self, name):
        card = self.findCardInHand(name)
        if not card:
            return
        if self.getResourcesBySphere(card.getSphere()) >= card.getCost():
            self.spendResourcesBySphere(card.getSphere(), card.getCost())
            self.addToAllies(card)

    def clearDeads(self):
        for hero in self.heroes:
            if hero.isDead():
                self.heroes.remove(hero)
        for ally in self.allies:
            if ally.isDead() or ally.getSphere() == 'Neutral':
                self.allies.remove(ally)

    def endTurn(self):
        self.increaseThreat(1)
        self.clearDeads()
        self.untapAll()
