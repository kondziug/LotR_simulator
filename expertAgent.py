from agent import Agent
from ally import Ally
import globals
import random

class ExpertAgent(Agent):
    def __init__(self, board, player):
        super(ExpertAgent, self).__init__(board, player)
    
    def expertPlanning(self):
        globals.dmode('Expert Planning Phase:')
        gandalf = self.player.findCardInHand('Gandalf')
        if not gandalf:
            return 
        if self.player.getResourcesBySphere(gandalf.sphere) < gandalf.cost:
            self.player.findAndSpend('Wandering Took')
            self.player.findAndSpend('Gondorian Spearman')
            self.player.findAndSpend('Veteran Axehand')
            globals.dmode('None')
            return
        if self.player.getResourcesBySphere(gandalf.sphere) >= gandalf.cost:
            self.player.spendResourcesBySphere(gandalf.sphere, gandalf.cost)
            self.player.addToAllies(gandalf)
            globals.dmode(gandalf.getName())
            return 

    def expertQuesting(self):
        globals.dmode('Expert Questing Phase:')
        combinedWillpower = 0
        spirits = self.player.getCharactersBySphere('Spirit')
        if not spirits:
            return 
        for card in spirits:
            combinedWillpower += card.getWillpower()
            card.tap()
            globals.dmode(card.getName())
        gandalf = self.player.findCardInPlay('Gandalf')
        if gandalf:
            combinedWillpower += gandalf.getWillpower()
            gandalf.tap()
            globals.dmode(gandalf.getName())
        # if combinedWillpower <= self.board.getCombinedThreat():
        #     return self.randomQuestingPhase() # but cards are already tapped !!!!!!!!!!!!
        self.resolveQuesting(combinedWillpower)

    def expertDefense(self): # to optimise!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11
        globals.dmode('Expert Defense Phase:')
        untapped = self.player.getUntappedCharacters()
        enemiesEngaged = self.board.getEnemiesEngaged()
        if not enemiesEngaged:
            globals.dmode('no enemies engaged')
            return
        for enemy in enemiesEngaged:
            if not untapped:
                self.player.randomUndefended(enemy.getAttack())
                continue
            defender = self.expertDefender(enemy, untapped)
            globals.dmode(defender.getName())
            result = defender.defense - enemy.attack
            if result < 0:
                defender.takeDamage(abs(result))
            defender.tap()
            untapped.remove(defender)

    @staticmethod
    def expertDefender(enemy, untapped):
        defender = None
        for card in untapped:
            if isinstance(card, Ally):
                defender = card
                return defender
        defender = random.choice(untapped)
        return defender

    def expertAttack(self): # to optimise !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        globals.dmode('Expert Attack Phase:')
        untapped = self.player.getUntappedCharacters()
        enemiesEngaged = self.board.getEnemiesEngaged()
        if not enemiesEngaged:
            globals.dmode('no enemies engaged')
            return
        if not untapped:
            globals.dmode('no player cards available')
            return
        for enemy in enemiesEngaged:
            if not untapped:
                return
            attacker = self.expertAttacker(enemy, untapped)
            if not attacker:
                continue
            globals.dmode(attacker.getName())
            result = enemy.defense - attacker.attack
            enemy.takeDamage(abs(result))
            if enemy.isDead():
                enemiesEngaged.remove(enemy)
            if not enemiesEngaged:
                return
            untapped.remove(attacker)

    @staticmethod
    def expertAttacker(enemy, untapped):
        attacker = None
        for card in untapped:
            if card.getAttack() > enemy.getDefense():
                attacker = card
                return attacker