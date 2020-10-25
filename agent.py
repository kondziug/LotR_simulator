import random

class Agent():
    def __init__(self, board, player):
        self.board = board
        self.player = player

    def resolveQuesting(self, combinedWillpower):
        self.board.addToStagingArea()
        result = combinedWillpower - self.board.getCombinedThreat()
        if result > 0:
            self.board.dealProgress(result)
        else:
            self.player.increaseThreat(abs(result))

    def encounterPhase(self):
        threat = self.player.getThreat()
        self.board.doEngagementChecks(threat)

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