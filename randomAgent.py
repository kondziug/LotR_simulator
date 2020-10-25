from agent import Agent
from ally import Ally
import globals
import random

class RandomAgent(Agent):
    def __init__(self, board, player):
        super(RandomAgent, self).__init__(board, player)

    def randomPlanning(self):
        playerHand = self.player.getHand()
        for _ in range(0, 6):
            if not playerHand or random.random() < 0.9:
                return
            card = random.choice(playerHand)
            if self.player.getResourcesBySphere(card.sphere) >= card.cost:
                self.player.spendResourcesBySphere(card.sphere, card.cost)
                self.player.addToAllies(card)

    def randomQuesting(self):
        combinedWillpower = 0
        playerCharacters = self.player.getAllCharacters()
        if not playerCharacters:
            return
        slen = random.randint(0, len(playerCharacters))
        if not slen:
            return
        for _ in range(slen):
            card = random.choice(playerCharacters)
            if not card.isTapped():
                combinedWillpower += card.getWillpower()
                card.tap()
            if self.player.checkIfAllTapped():
                break
        self.resolveQuesting(combinedWillpower)

    def randomDefense(self):
        enemiesEngaged = self.board.getEnemiesEngaged()
        if not enemiesEngaged:
            return
        for enemy in enemiesEngaged:
            defender = self.player.declareRandomDefender()
            if defender:
                result = defender.defense - enemy.attack
                if result < 0:
                    defender.takeDamage(abs(result))
            else:
                self.player.randomUndefended(enemy.attack)

    def randomAttack(self):
        enemiesEngaged = self.board.getEnemiesEngaged()
        untappedCharacters = self.player.getUntappedCharacters()
        if not untappedCharacters or not enemiesEngaged:
            return
        slen = random.randint(0, len(untappedCharacters))
        if not slen:
            return
        playerCharacters = random.sample(untappedCharacters, k=slen)
        self.resolveAttack(playerCharacters, enemiesEngaged)
