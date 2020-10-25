from card import Card

class Creature(Card):
    def __init__(self, name, attack, defense, hitpoints):
        super(Creature, self).__init__(name)
        self.attack = attack
        self.defense = defense
        self.hitpoints = hitpoints

    def getAttack(self):
        return self.attack

    def getDefense(self):
        return self.defense

    def getHitpoints(self):
        return self.hitpoints

    def setHitpoints(self, hitpoints):
        self.hitpoints = hitpoints

    def isDead(self):
        return self.getHitpoints() <= 0

    def takeDamage(self, damage):
        self.hitpoints -= damage
