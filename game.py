from expertAgent import ExpertAgent
from randomAgent import RandomAgent
import random
import globals

class Game():
    def __init__(self, board, player):
        self.board = board
        self.player = player
        self.turn = 0

    def getBoard(self):
        return self.board

    def getPlayer(self):
        return self.player

    def getTurnNumber(self):
        return self.turn

    def copy(self):
        newGame = Game(self.board, self.player)
        newGame.turn = self.turn
        return newGame

    def setupGame(self):
        # self.board.scenarioSetup()
        self.player.shufflePlayerDeck()
        self.player.drawHand()

    def resourcePhase(self):
        self.player.readyTurn()

    def playoutPlanningPhase(self): 
        playerHand = self.player.getHand()
        for _ in range(0, 6):
            card = random.choice(playerHand)
            if self.player.getResourcesBySphere(card.sphere) >= card.cost:
                self.player.spendResourcesBySphere(card.sphere, card.cost)
                self.player.addToAllies(card)

    # def playoutQuestingPhase1(self): 
    #     combinedWillpower = 0
    #     playerCharacters = self.player.getAllCharacters()
    #     if not playerCharacters:
    #         return
    #     slen = random.randint(0, len(playerCharacters))
    #     if not slen:
    #         return
    #     for _ in range(slen):
    #         card = random.choice(playerCharacters)
    #         if not card.isTapped():
    #             combinedWillpower += card.getWillpower()
    #             card.tap()
    #         if self.player.checkIfAllTapped():
    #             break
    #     self.resolveQuesting(combinedWillpower)
        
    def playoutQuestingPhase(self):
        combinedWillpower = 0
        playerCharacters = self.player.getAllCharacters()
        if not playerCharacters:
            return
        while combinedWillpower <= self.board.getCombinedThreat():
            card = random.choice(playerCharacters)
            if not card.isTapped():
                combinedWillpower += card.getWillpower()
                card.tap()
            if self.player.checkIfAllTapped():
                break
        self.board.addToStagingArea()
        self.resolveQuesting(combinedWillpower)

    def resolveQuesting(self, combinedWillpower):
        result = combinedWillpower - self.board.getCombinedThreat()
        if result > 0:
            self.board.dealProgress(result)
        else:
            self.player.increaseThreat(abs(result))

    def randomTravelPhase(self):
        activeLand = self.board.getActiveLand()
        if activeLand:
            return
        lands = self.board.getAllLands()
        if not lands:
            return
        land = random.choice(lands)
        self.board.travelToLocation(land)

    def encounterPhase(self):
        threat = self.player.getThreat()
        self.board.doEngagementChecks(threat)

    def playoutCombatPhase(self):
        self.playoutDefense()
        self.playoutAttackEnemies()

    def playoutDefense(self):
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

    def playoutAttackEnemies(self):
        enemiesEngaged = self.board.getEnemiesEngaged()
        untappedCharacters = self.player.getUntappedCharacters()
        if not untappedCharacters or not enemiesEngaged:
            return
        slen = random.randint(0, len(untappedCharacters))
        if not slen:
            return
        playerCharacters = random.sample(untappedCharacters, k=slen)
        self.resolveAttack(playerCharacters, enemiesEngaged)

    def applyCard(self, name):
        card = self.board.getEncounterDeck().findCopyOfCard(name)
        self.board.addCard(card)
        self.board.getEncounterDeck().getCardList().remove(card)

    def subsetPlanning(self, subset):
        if not subset:
            return
        for name in subset.getCardList():
            if name == 'None':
                return
            card = self.player.findCardInHand(name)
            self.player.spendResourcesBySphere(card.sphere, card.cost)
            self.player.addToAllies(card)

    def subsetQuesting(self, subset, withStaging):
        if not subset:
            return
        combinedWillpower = 0
        for name in subset:
            card = self.player.findCardInPlay(name)
            combinedWillpower += card.getWillpower()
            card.tap()
        if withStaging:
            self.board.addToStagingArea()
        self.resolveQuesting(combinedWillpower)

    def subsetDefense(self, subset):
        if not subset:
            return
        enemiesEngaged = self.board.getEnemiesEngaged()
        if not enemiesEngaged: # to remove??????????????
            return
        playerCharacters = []
        for name in subset:
            card = self.player.findCardInPlay(name)
            playerCharacters.append(card)
        for enemy in enemiesEngaged:
            defender = random.choice(playerCharacters)
            if not defender.isTapped():
                result = defender.defense - enemy.attack
                if result < 0:
                    defender.takeDamage(abs(result))
                defender.tap()
            else:
                defender.takeDamage(enemy.attack)
            playerCharacters.remove(defender)

    def subsetAttack(self, subset):
        if not subset:
            return
        enemiesEngaged = self.board.getEnemiesEngaged()
        playerCharacters = []
        for name in subset.getCardList():
            card = self.player.findCardInPlay(name)
            playerCharacters.append(card)
        self.resolveAttack(playerCharacters, enemiesEngaged)

    def resolveAttack(self, playerCharacters, enemiesEngaged):
        for character in playerCharacters:
            randomTarget = random.choice(enemiesEngaged)
            result = randomTarget.defense - character.attack
            if result < 0:
                randomTarget.takeDamage(abs(result))
                if randomTarget.isDead():
                    enemiesEngaged.remove(randomTarget)
            if not enemiesEngaged:
                return

    def randomPlanning(self):
        randomAgent = RandomAgent(self.board, self.player)
        randomAgent.randomPlanning()

    def randomQuesting(self):
        randomAgent = RandomAgent(self.board, self.player)
        randomAgent.randomQuesting()

    def randomDefense(self):
        randomAgent = RandomAgent(self.board, self.player)
        randomAgent.randomDefense()

    def randomAttack(self):
        randomAgent = RandomAgent(self.board, self.player)
        randomAgent.randomAttack()

    def expertPlanning(self):
        expertAgent = ExpertAgent(self.board, self.player)
        expertAgent.expertPlanning()

    def expertQuesting(self):
        expertAgent = ExpertAgent(self.board, self.player)
        expertAgent.expertQuesting()

    def expertDefense(self):
        expertAgent = ExpertAgent(self.board, self.player)
        expertAgent.expertDefense()

    def expertAttack(self):
        expertAgent = ExpertAgent(self.board, self.player)
        expertAgent.expertAttack()
            
    def refreshPhase(self):
        self.board.endTurn()
        self.player.endTurn()
        self.turn += 1

    # def doTurn(self):
    #     self.resourcePhase()
    #     self.playoutPlanningPhase()
    #     self.playoutQuestingPhase()
    #     self.randomTravelPhase()
    #     self.encounterPhase()
    #     self.playoutCombatPhase()
    #     self.refreshPhase()

    # def completeTurn(self):
    #     self.playoutQuestingPhase()
    #     self.randomTravelPhase()
    #     self.encounterPhase()
    #     self.playoutCombatPhase()
    #     self.refreshPhase()

    ######################## random playout ####################
    # def doTurn(self):
    #     self.resourcePhase()
    #     self.randomPlanning()
    #     self.randomQuesting()
    #     self.randomTravelPhase()
    #     self.encounterPhase()
    #     self.randomDefense()
    #     self.randomAttack()
    #     self.refreshPhase()

    # def completeTurn(self):
    #     self.randomQuesting()
    #     self.randomTravelPhase()
    #     self.encounterPhase()
    #     self.randomDefense()
    #     self.randomAttack()
    #     self.refreshPhase()

    ######################## expert playout ####################
    def doTurn(self):
        self.resourcePhase()
        self.expertPlanning()
        self.expertQuesting()
        self.randomTravelPhase()
        self.encounterPhase()
        self.expertDefense()
        self.expertAttack()
        self.refreshPhase()

    def completeTurn(self):
        self.expertQuesting()
        self.randomTravelPhase()
        self.encounterPhase()
        self.expertDefense()
        self.expertAttack()
        self.refreshPhase()
