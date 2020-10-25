from hero import Hero
from ally import Ally
from quest import Quest
from enemy import Enemy
from land import Land
from quest_deck import QuestDeck
from regular_deck import RegularDeck

def init():
    global gameOver
    global gameWin
    gameOver = False
    gameWin = False

    global dictOfCards
    global heroes
    global decks
    dictOfCards = {}
    heroes = []
    decks = {}

    dictOfCards['Eowyn'] = Hero('Eowyn', 1, 1, 3, 4, 'Spirit', 9)
    dictOfCards['Eleanor'] = Hero('Eleanor', 1, 2, 3, 1, 'Spirit', 7)
    dictOfCards['Thalin'] = Hero('Thalin', 2, 2, 4, 1, 'Tactics', 9)
    dictOfCards['Wandering Took'] = Ally('Wandering Took', 1, 1, 2, 1, 'Spirit', 2)
    dictOfCards['Lorien Guide'] = Ally('Lorien Guide', 1, 1, 2, 0, 'Spirit', 3)
    dictOfCards['Northern Tracker'] = Ally('Northern Tracker', 2, 2, 3, 1, 'Spirit', 4)
    dictOfCards['Veteran Axehand'] = Ally('Veteran Axehand', 2, 1, 2, 0, 'Tactics', 2)
    dictOfCards['Gondorian Spearman'] = Ally('Gondorian Spearman', 1, 1, 1, 0, 'Tactics', 2)
    dictOfCards['Horseback Archer'] = Ally('Horseback Archer', 2, 1, 2, 0, 'Tactics', 3)
    dictOfCards['Beorn'] = Ally('Beorn', 3, 3, 6, 1, 'Tactics', 6)
    dictOfCards['Gandalf'] = Ally('Gandalf', 4, 4, 4, 4, 'Neutral', 5)

    dictOfCards['Flies and Spiders'] = Quest('Flies and Spiders', 'Passage through Mirkwood', 8)
    dictOfCards['A fork in the road'] = Quest('A fork in the road', 'Passage through Mirkwood', 2)
    dictOfCards['Beorns Path'] = Quest('Beorns Path', 'Passage through Mirkwood', 10)

    dictOfCards['Dol Guldur Orcs'] = Enemy('Dol Guldur Orcs', 2, 0, 3, 10, 2)
    dictOfCards['Chieftan Ufthak'] = Enemy('Chieftan Ufthak', 3, 3, 6, 35, 2)
    dictOfCards['Dol Guldur Beastmaster'] = Enemy('Dol Guldur Beastmaster', 3, 1, 5, 35, 2)
    dictOfCards['Necromancers Pass'] = Land('Necromancers Pass', 3, 2)
    dictOfCards['Enchanted Stream'] = Land('Enchanted Stream', 2, 2)
    dictOfCards['Forest Spider'] = Enemy('Forest Spider', 2, 1, 4, 25, 2)
    dictOfCards['Old Forest Road'] = Land('Old Forest Road', 1, 3)
    dictOfCards['East Bight Patrol'] = Enemy('East Bight Patrol', 3, 1, 2, 5, 3)
    dictOfCards['Black Forest Bats'] = Enemy('Black Forest Bats', 1, 0, 2, 15, 1)
    dictOfCards['Forest Gate'] = Land('Forest Gate', 2, 4)
    dictOfCards['King Spider'] = Enemy('King Spider', 3, 1, 3, 20, 2)
    dictOfCards['Hummerhorns'] = Enemy('Hummerhorns', 2, 0, 3, 40, 1)
    dictOfCards['Ungoliants Spawn'] = Enemy('Ungoliants Spawn', 5, 2, 9, 32, 3)
    dictOfCards['Great Forest Web'] = Land('Great Forest Web', 2, 2)
    dictOfCards['Mountains of Mirkwood'] = Land('Mountains of Mirkwood', 2, 3)

    heroes.append(dictOfCards['Eowyn'])
    heroes.append(dictOfCards['Eleanor'])
    heroes.append(dictOfCards['Thalin'])

    playerDeck = RegularDeck('Player Deck')
    playerDeck.addCard(dictOfCards['Wandering Took'], 3)
    playerDeck.addCard(dictOfCards['Lorien Guide'], 3)
    playerDeck.addCard(dictOfCards['Northern Tracker'], 3)
    playerDeck.addCard(dictOfCards['Veteran Axehand'], 3)
    playerDeck.addCard(dictOfCards['Gondorian Spearman'], 3)
    playerDeck.addCard(dictOfCards['Horseback Archer'], 3)
    playerDeck.addCard(dictOfCards['Beorn'], 1)
    playerDeck.addCard(dictOfCards['Gandalf'], 3)
    decks['Player Deck'] = playerDeck

    questDeck = QuestDeck('Passage through Mirkwood')
    questDeck.addCard(dictOfCards['Flies and Spiders'], 1)
    decks['Quest Deck'] = questDeck

    # encounterDeck = RegularDeck('Encounter Deck')
    # encounterDeck.addCard(dictOfCards['Dol Guldur Orcs'], 4)
    # encounterDeck.addCard(dictOfCards['Enchanted Stream'], 4)
    # encounterDeck.addCard(dictOfCards['Black Forest Bats'], 4)
    # encounterDeck.addCard(dictOfCards['Hummerhorns'], 4)
    # encounterDeck.addCard(dictOfCards['Old Forest Road'], 4)
    # encounterDeck.addCard(dictOfCards['Forest Spider'], 4)
    # encounterDeck.addCard(dictOfCards['East Bight Patrol'], 4)
    # decks['Encounter Deck'] = encounterDeck


    # ---------------- Full Version -----------------------------

    # questDeck = QuestDeck('Passage through Mirkwood')
    # questDeck.addCard(dictOfCards['Flies and Spiders'], 1)
    # questDeck.addCard(dictOfCards['A fork in the road'], 1)
    # questDeck.addCard(dictOfCards['Beorns Path'], 1)
    # decks['Quest Deck'] = questDeck
    
    encounterDeck = RegularDeck('Encounter Deck')
    encounterDeck.addCard(dictOfCards['Dol Guldur Orcs'], 3)
    encounterDeck.addCard(dictOfCards['Chieftan Ufthak'], 1)
    encounterDeck.addCard(dictOfCards['Dol Guldur Beastmaster'], 2)
    encounterDeck.addCard(dictOfCards['Necromancers Pass'], 2)
    encounterDeck.addCard(dictOfCards['Enchanted Stream'], 2)
    encounterDeck.addCard(dictOfCards['Forest Spider'], 4)
    encounterDeck.addCard(dictOfCards['Old Forest Road'], 2)
    encounterDeck.addCard(dictOfCards['East Bight Patrol'], 1)
    encounterDeck.addCard(dictOfCards['Black Forest Bats'], 1)
    encounterDeck.addCard(dictOfCards['Forest Gate'], 2)
    encounterDeck.addCard(dictOfCards['King Spider'], 2)
    encounterDeck.addCard(dictOfCards['Hummerhorns'], 1)
    encounterDeck.addCard(dictOfCards['Ungoliants Spawn'], 1)
    encounterDeck.addCard(dictOfCards['Great Forest Web'], 2)
    encounterDeck.addCard(dictOfCards['Mountains of Mirkwood'], 3)
    decks['Encounter Deck'] = encounterDeck

def setupEasy():
    global decks

    decks['Encounter Deck'] = {}
    encounterDeck = RegularDeck('Encounter Deck')
    encounterDeck.addCard(dictOfCards['Dol Guldur Orcs'], 4)
    encounterDeck.addCard(dictOfCards['Enchanted Stream'], 4)
    encounterDeck.addCard(dictOfCards['Black Forest Bats'], 4)
    encounterDeck.addCard(dictOfCards['Hummerhorns'], 4)
    encounterDeck.addCard(dictOfCards['Old Forest Road'], 4)
    encounterDeck.addCard(dictOfCards['Forest Spider'], 4)
    encounterDeck.addCard(dictOfCards['East Bight Patrol'], 4)
    decks['Encounter Deck'] = encounterDeck


def dmode(msg):
    verbose = False
    if verbose:
        print(msg)

